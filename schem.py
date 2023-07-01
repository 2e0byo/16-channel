from skidl import *
from firmware.hal import hal

# skidl_cfg.store()

# Power nets
GND_PWR = Net("GND_PWR")
GND = Net("GND")
FIVE_V = Net("+5V")
THREE_V = Net("+3V3")
HV = Net("HV")
HV_UPSTREAM = Net("HV_UPSTREAM")

# Buses
# Avoid global shared nets even for single items.  Conceptually these are buses.
mkbus = lambda a, *b: Bus(a, [Net(x) for x in b])
buses = dict(
    I2C=mkbus("I2C", "SDA", "SCL"),
    SPI=mkbus("SPI", "MISO", "CLK", "CS"),  # mosi unused
    LCD=mkbus("LCD", "VO", "RS", "E", "D4", "D5", "D6", "D7", "Backlight"),
    ATX_CTL=mkbus("ATX_CTL", "PWR_ON"),
    SHUTOFF=mkbus("SHUTOFF", "OE"),
    MCU_CTL=mkbus("MCU_CTL", "EN", "IO0", "TXD", "RXD"),
    IO=mkbus("IO", "R1", "R2", "Switch"),
)


def module(fn):
    """
    Immediately define a module, using the function only for documentation.

    This differs from the encapsulation provided by @package
    """
    print(f"Constructing {fn.__name__}...", end="", flush=True)
    fn()
    print("done!")


def Led(color="red", **kwargs):
    kwargs["footprint"] = kwargs.get("footprint", "LED_0603_1608Metric")
    return Part("Device", "LED", **kwargs)


def R(value, **kwargs):
    kwargs.pop("value", None)
    kwargs["footprint"] = kwargs.get("footprint", "R_0603_1608Metric")
    return Part("Device", "R", value=value, **kwargs)


def C(value, **kwargs):
    kwargs.pop("value", None)
    kwargs["footprint"] = kwargs.get("footprint", "C_0603_1608Metric")
    return Part("Device", "C", value=value, **kwargs)


def NPN():
    return Part("easyeda", "SS8050-G", footprint="SOT-23-3")


def connections(pin):
    def sum_net(n):
        pins = n.pins[:]
        pins.remove(pin)
        named_net = not n.name.startswith("N$")
        # Assume manually named nets will be connected elsewhere at least once
        return len(pins) + int(named_net)

    return sum(sum_net(n) for n in pin.nets)


def channel() -> Part:
    inr = R("100R", ref="channel_in")
    driver = Part("Driver_FET", "ZXGD3003E6", footprint="SOT-23-6")
    driver["IN1"] += driver["IN2"]
    driver["SOURCE"] += driver["SINK"]
    driver["GND"] += GND_PWR
    driver["VCC"] += HV
    driver["IN1"] += inr[2]

    upper_pad = Part(
        "Connector_Generic",
        "Conn_01x01",
        ref="pad",
        footprint="SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm",
    )
    lower_pad = upper_pad.copy()
    backemf_diode = Part("easyeda", "S5DC-13-F", footprint="D_SMC")
    mosfet = Part("easyeda", "AOD508", footprint="TO-252-3_L6.5-W5.8-P4.58-BR")

    HV & upper_pad & backemf_diode["K,A"] & lower_pad & mosfet["D,S"] & GND_PWR
    pulldown = R("100K", ref="channel_pulldown")
    mosfet["G"] & pulldown & GND_PWR
    driver["SOURCE"] & R("1R") & mosfet["G"]

    return inr[1]


def buffer(not_oe):
    nor = Part("74xx", "74HC04", footprint="SOIC-14_3.9x8.7mm_P1.27mm")
    nor["GND"] += GND
    nor["VCC"] += THREE_V
    # unused
    for p in range(3, 7):
        nor[f"{p}A"] += GND
        nor[f"{p}Y"] += NC
    pullup = R("10K", ref="buffer_pullup")
    THREE_V & pullup & nor["1A"]
    OE = Net("OE")
    nor["1A"] += OE
    nor["1Y"] += not_oe
    nor["2A"] += nor["1A"]
    overcurrent = Led()
    current_limiting = R("2K", ref="buffer_led_r")
    THREE_V & overcurrent & current_limiting & nor["2Y"]


@module
def led_driver():
    driver = Part("Driver_LED", "PCA9685PW", footprint="TSSOP-28_8x9.7mm_P0.65mm")
    driver["A0, A2, A4, VDD"] += FIVE_V
    driver["A1, A3, A5, EXTCLK, VSS"] += GND
    decoupling = C("100n")
    driver["VDD"] & decoupling & GND
    not_oe = Net("~OE")
    driver["~OE"] += not_oe
    driver["SDA, SCL"] += buses["I2C"]
    channels = [channel() for _ in range(16)]
    driver[", ".join(f"LED{x}" for x in range(16))] += channels
    buffer(not_oe)


@module
def power_in():
    global GND_PWR
    # power in
    atx = Part(
        "Connector",
        "ATX-24",
        footprint="Molex_Mini-Fit_Jr_5566-24A_2x12_P4.20mm_Vertical",
    )
    atx[:] += NC
    atx["GND"] += GND
    atx["PS_ON#"] += buses["ATX_CTL"]["PWR_ON"]
    atx["+12V"] += HV_UPSTREAM
    atx["+5VSB"] += FIVE_V
    FIVE_V.drive = POWER

    eps12v = Part(
        "easyeda",
        "EPS12V",
        footprint="Molex_Mini-Fit_Jr_5566-08A_2x04_P4.20mm_Vertical",
    )
    eps12v["+12V"] += HV_UPSTREAM
    eps12v["GND"] += GND_PWR
    GND_PWR += GND
    GND_PWR.drive = POWER
    HV_UPSTREAM.drive = POWER


@module
def regulator():
    reg = Part("Regulator_Linear", "AMS1117-3.3", footprint="SOT-89-3")
    reg["GND"] += GND
    reg["VI"] += FIVE_V
    reg["VI"] & C("22u") & GND
    reg["VO"] += THREE_V
    reg["VO"] & C("22u") & GND
    reg["VO"] & R("2K") & Led("red") & GND


@module
def UI():
    lcd = Part(
        "Connector_Generic", "Conn_01x16", footprint="PinHeader_1x16_P2.54mm_Vertical"
    )
    lcd[:] += NC
    pins = "VSS VDD VO RS RW E D0 D1 D2 D3 D4 D5 D6 D7 A K"
    for i, pin in enumerate(pins.split()):
        lcd[i + 1].aliases += pin
    lcd["E, VSS"] += GND
    lcd["VDD"] += FIVE_V
    lcd["A"] & R("220R") & FIVE_V
    q = NPN()
    q["E"] += GND
    q["C"] += lcd["K"]
    q["B"] & R("1K") & buses["LCD"]["Backlight"]
    for net, name in ((n, n.name) for n in buses["LCD"] if n.name != "Backlight"):
        lcd[name] += net

    Switch = Part(
        "Switch", "SW_Push", dest=TEMPLATE, footprint="KEY-SMD_L6.2-W3.6-LS8.0"
    )
    boot, enable = Switch(2)
    boot[1] += GND
    boot[2] & C("100n") & GND
    boot[2] += buses["MCU_CTL"]["IO0"]
    enable[1] += GND
    enable[2] & C("100n") & GND
    enable[2] += buses["MCU_CTL"]["EN"]

    encoder = Part(
        "Device",
        "Rotary_Encoder_Switch",
        footprint="RotaryEncoder_Bourns_Horizontal_PEC12R-2xxxF-Sxxxx",
    )
    encoder["C, S2"] += GND
    for p in {"A", "B", "S1"}:
        encoder[p] & R("100K") & THREE_V
    encoder["S2"] += buses["IO"]["Switch"]
    encoder["A"] += buses["IO"]["R1"]
    encoder["B"] += buses["IO"]["R2"]


@module
def monitoring():
    temperature = Part(
        "easyeda", "LM75AD", footprint="SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm"
    )
    temperature["A0, A1, A2, GND"] += GND
    temperature["VCC"] += THREE_V
    temperature["VCC"] & C("100n") & GND
    temperature["OS"] += buses["SHUTOFF"]["OE"]
    for p in {"SCL", "SDA"}:
        temperature[p] += buses["I2C"][p]

    current_sensor = Part(
        "easyeda",
        "ACS71240LLCBTR-030B3",
        footprint="SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm",
    )
    current_sensor["VCC"] += THREE_V
    current_sensor["VCC"] & C("100n") & GND
    current_sensor["GND"] += GND
    current_sensor["IP+"] += HV_UPSTREAM
    current_sensor["IP-"] += HV
    current_sensor["~{FAULT}"] += buses["SHUTOFF"]["OE"]

    # current sensor output is bidirectional; vcc/2 for 0A
    # scale for full range on the +ve side and filter

    # generic lm358 clone; low bandwidth op amps fine here
    op_amp = Part(
        "easyeda", "AP358SG-13", footprint="SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm"
    )
    op_amp["GND"] += GND
    op_amp["VCC"] += FIVE_V  # give it some headroom
    op_amp["VCC"] & C("1u") & GND
    op_amp["OUTPUT2"] += NC
    op_amp["IN2-, IN2+"] += GND

    # differential amplifier
    THREE_V & R("24K") & op_amp["IN1-"] & R("24K") & GND
    op_amp["OUTPUT1"] & R("30K") & op_amp["IN1-"]
    op_amp["IN1+"] & R("30K") & GND
    # LPF with input R
    op_amp["IN1+"] & C("100n") & GND
    op_amp["IN1+"] & R("12K") & current_sensor["VIOUT"]

    adc = Part("Analog_ADC", "MCP3201", footprint="SOP-8_3.9x4.9mm_P1.27mm")
    adc["Vdd", "Vref"] += THREE_V
    adc["Vdd"] & C("100n") & GND
    adc["Vss, IN-"] += GND
    # series R vain attempt to protect from 5v output...
    adc["IN+"] & R("10R") & op_amp["OUTPUT1"]
    adc["Dout"] += buses["SPI"]["MISO"]
    adc["~CS~/SHDN"] += buses["SPI"]["CS"]
    adc["CLK"] += buses["SPI"]["CLK"]


@module
def usb():
    socket = Part("easyeda", "YTC-TC16S-26", footprint="USB-C-SMD_YTC-TC16S-26-A")
    socket["GND"] += GND
    mounting_pins = socket[12, 13, 14, 15]
    mounting_pins += GND
    socket["SBU1", "SBU2"] += NC
    # usb 3.2 requires signalling that we're sink only
    socket["CC1"] & R("5K1") & GND
    socket["CC2"] & R("5K1") & GND
    d_plus = socket["DP1, DP2"]
    d_minus = socket["DN1, DN2"]
    vbus = socket["VBUS"]

    clamp_diodes = Part(
        "easyeda", "RCLAMP7534P-N", footprint="DFN2010-5L_L2.0-W1.0-P0.8-BL"
    )
    clamp_diodes["GND"] += GND
    clamp_diodes[5] += d_plus
    clamp_diodes[4] += d_minus
    clamp_diodes[1] += vbus
    clamp_diodes[3] += NC

    interface = Part(
        "Interface_USB",
        "CP2102N-A01-GQFN28",
        footprint="QFN-28_L5.0-W5.0-P0.50-TL-EP3.3",
    )
    interface[:] += NC
    interface["GND"] += GND
    interface["VDD, REGIN"] += THREE_V
    decoupling = C("100n") | C("4.7u")
    interface["VDD"] & decoupling & GND
    interface["~RSTb"] & R("2K") & THREE_V
    vbus & R("22K1") & (R("47K5") & GND) & interface["VBUS"]
    interface["D+"] += d_plus
    interface["D-"] += d_minus

    # zero ohm resistors in case we need to cut the track
    interface["TXD"] & R("0") & buses["MCU_CTL"]["TXD"]
    interface["RXD"] & R("0") & buses["MCU_CTL"]["RXD"]

    # pull lines to state of other pin.  This logic is used by esptool.py
    q1, q2 = NPN(), NPN()
    q1["C"] += buses["MCU_CTL"]["EN"]
    q1["B"] & R("10K") & interface["~DTR"]
    q1["E"] & interface["~RTS"]

    q2["C"] += buses["MCU_CTL"]["IO0"]
    q2["E"] += interface["~DTR"]
    q2["B"] & R("10K") & interface["~RTS"]


@module
def mcu():
    soc = Part("RF_Module", "ESP32-WROOM-32D", footprint="ESP32-WROOM-32D")
    soc["GND"] += GND
    soc["VDD"] += THREE_V
    decoupling = C("22u") | C("100n")
    soc["VDD"] & decoupling & GND
    soc["SENSOR_VP"].aliases += "IO36"
    soc["SENSOR_VN"].aliases += "IO39"
    soc["NC"] += NC

    no_erc = {"EN"}
    for bus, conns in hal.items():
        for pin, iface in conns.items():
            if bus == "PINS":
                soc[pin] += iface.r[1]
            else:
                # use explicit name to catch out-of-order errors
                assert buses[bus][
                    iface.name
                ], f"bus {bus} does not contain {iface.name}"
                assert soc[pin], f"No such pin {pin}"
                assert iface.r, f"No resistor for {iface}"
                soc[pin] & iface.r & buses[bus][iface.name]
            if pin not in no_erc:
                erc_assert(
                    f"connections(soc['{pin}']) ==1",
                    f"Multiple connections on pin {pin} of soc.",
                )

    reverse = lambda d: {v.name: v.r[2] for v in d.values()}

    pins = reverse(hal["PINS"])
    pins["Status"] & Led("green") & GND
    power_on_reset = R("10K") & soc["EN"] & C("100n") & GND
    soc["EN"] += power_on_reset

    pins = reverse(hal["I2C"])
    # bus pullups belong at master
    pins["SDA"] & R("2K2") & THREE_V
    pins["SCL"] & R("2K2") & THREE_V

    # make unused pins available later
    for pin in (p for p in soc.pins if not connections(p)):
        pin & R("10R") & NC


@module
def io():
    i2c_out = Part(
        "Connector", "Conn_01x04_Male", footprint="PinHeader_1x04_P2.54mm_Vertical"
    )
    # skidl slice is inclusive...
    i2c_out[1:2] += [THREE_V, GND]
    i2c_out[3:] += buses["I2C"]


if __name__ == "__main__":
    buses["SHUTOFF"]["OE"].do_erc = False
    ERC()
    generate_netlist()
