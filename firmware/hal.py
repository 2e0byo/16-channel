from collections import namedtuple

Pin = namedtuple("Pin", ("name", "input"))


class Interface:
    def __init__(self, name: str, series_r: str = "10R", input=False):
        self.name = name
        self.value = series_r
        self._r = None
        self.input = input

    @property
    def r(self):
        from skidl import R

        if not self._r:
            self._r = R(self.value, ref=self.name)
        return self._r


hal = {
    "LCD": {
        "IO32": Interface("VO"),
        "IO33": Interface("RS"),
        "IO25": Interface("E"),
        "IO26": Interface("D4"),
        "IO27": Interface("D5"),
        "IO14": Interface("D6"),
        "IO13": Interface("D7"),
        "IO4": Interface("Backlight", "2K"),
    },
    "I2C": {
        "IO22": Interface("SDA"),
        "IO21": Interface("SCL"),
    },
    "SHUTOFF": dict(IO23=Interface("OE")),
    "ATX_CTL": {"IO16": Interface("PWR_ON", input=True)},
    "MCU_CTL": {
        "TXD0/IO1": Interface("TXD"),
        "RXD0/IO3": Interface("RXD"),
        "IO0": Interface("IO0"),
        "EN": Interface("EN"),
    },
    "IO": {
        "IO34": Interface("R1", input=True),
        "IO35": Interface("R2", input=True),
        "IO36": Interface("Switch", input=True),
    },
    "SPI": {
        "IO18": Interface("MISO"),
        "IO5": Interface("CLK"),
        "IO17": Interface("CS"),
    },
    "PINS": {"IO2": Interface("Status", "2K")},
}


def _as_dict(d: "dict[str, Interface] | dict[str, dict]"):
    resolved = {}
    for k, v in d.items():
        if isinstance(v, Interface):
            resolved[v.name] = Pin(k, v.input)
        elif isinstance(v, dict):
            resolved[k] = _as_dict(v)
        else:
            raise ValueError(f"Unknown value type {type(v)}")
    return resolved


static_hal = _as_dict(hal)
