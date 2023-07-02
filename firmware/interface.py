from hal import static_hal
from machine import Pin, SPI, I2C, SoftI2C, UART
import hal
from pca9685 import PCA9685


def make_spi(**mapping):
    return SPI(
        baudrate=1000000,
        polarity=0,
        phase=0,
        bits=8,
        sck=translate_pin(mapping["CLK"]),
        mosi=translate_pin(mapping["MOSI"]),
        miso=translate_pin(mapping["MISO"]),
        cs=translate_pin(mapping["CS"]),
    )


_i2c = 0


def make_i2c(**mapping):
    global _i2c
    scl, sda = translate_pin(mapping["SCL"]), translate_pin(mapping["SDA"])
    try:
        i2c = I2C(_i2c, scl=scl, sda=sda)
        _i2c += 1
    except ValueError:
        i2c = SoftI2C(scl=scl, sda=sda)
    return i2c


def translate_pin(pin: hal.Pin) -> Pin:
    print(pin)
    direction = Pin.IN if pin.input else Pin.OUT
    special_names: dict[str, int] = {}
    return Pin(special_names.get(pin.name, int(pin.name[2:])), direction)


def make_pins(**mapping):
    return {k: translate_pin(v) for k, v in mapping.items() if v not in skip_pins}


bus_types = {
    "SPI": make_spi,
    "I2C": make_i2c,
}

skip_pins = ("EN", "TXD0/IO1", "RXD0/IO3", "IO0")
skip_buses = ("MCU_CTL", "SPI")

buses = {
    k: bus_types.get(k, make_pins)(**v)
    for k, v in static_hal.items()
    if k not in skip_buses
}


def psu(state: "bool | None" = None) -> bool:
    p = buses["ATX_CTL"]["PWR_ON"]
    if state:
        p.init(p.OUT, value=0)
    elif state is not None:
        p.init(p.IN)
    return not p.value()


controller = PCA9685(buses["I2C"])
