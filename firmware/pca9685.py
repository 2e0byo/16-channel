from machine import I2C
import time


import ustruct
import time


class Controller:
    def __init__(self):
        self.entered = False

    def set_pwm(self, channel: int, on_t: int, off_t: int) -> None:
        if not self.entered:
            raise RuntimeError(
                f"{self.__class__.__name__} should be used as a context manager."
            )
        return self._set_pwm(channel, on_t, off_t)

    def _set_pwm(self, channel: int, on_t: int, off_t: int) -> None:
        raise NotImplementedError()

    def get_pwm(self, channel: int) -> tuple[int, int]:
        if not self.entered:
            raise RuntimeError(
                f"{self.__class__.__name__} should be used as a context manager."
            )
        return self._get_pwm(channel)

    def _get_pwm(self, channel: int) -> tuple[int, int]:
        raise NotImplementedError()

    def _setup(self):
        raise NotImplementedError()

    def _reset(self):
        raise NotImplementedError()

    def __enter__(self) -> "Controller":
        self._setup()
        self._reset()
        self.entered = True
        return self

    def __exit__(self, *_):
        self.entered = False
        self._reset()

    def frequency(self, val_hz: "int | None" = None) -> int:
        raise NotImplementedError()


class Channel:
    def __init__(self, controller: Controller, channel: int, offset: int):
        self.controller = controller
        self.channel = channel
        if offset > 4095 or offset < 0:
            raise ValueError("Offset must be between 0 and 4095")
        self.offset = offset

    def brightness(self, value: "int | None" = None) -> int:
        if value is not None:
            value = max(0, min(value, 4095))
            on = self.offset
            off = (self.offset + value) % 4096
            self.controller.set_pwm(self.channel, on, off)
        on, off = self.controller.get_pwm(self.channel)
        period = off - on
        if period < 0:
            period += 4096
        return period

    def percent_brightness(self, value: "float | None" = None) -> float:
        if value is not None:
            value = max(0, min(1, value))
            self.brightness(round(value * 4096))
        brightness = self.brightness()
        return brightness / 4096 if brightness != 4095 else 1


class PCA9685(Controller):
    def __init__(self, i2c: I2C, address: int = 0x40, clk_hz: int = 25_000_000):
        self.i2c = i2c
        self.address = address
        self.channels = [Channel(self, i, i * 256) for i in range(16)]
        self.clk_hz = clk_hz
        super().__init__()

    def _write(self, address: int, data: bytes):
        self.i2c.writeto_mem(self.address, address, data)

    def _read(self, address: int, nbytes: int) -> bytes:
        return self.i2c.readfrom_mem(self.address, address, nbytes)

    def _setup(self):
        self._write(0x00, b"\x20")  # Auto increment on

    def _reset(self):
        self._write(0xFA, b"\x00\x00\x00\x00")  # Turn off all outputs

    def _set_pwm(self, channel: int, on_t: int, off_t: int) -> None:
        offset = 4 * channel  # registers are ON_L, ON_H, OFF_L, OFF_H
        self._write(6 + offset, on_t.to_bytes(2, "little"))
        self._write(8 + offset, off_t.to_bytes(2, "little"))

    def _get_pwm(self, channel: int) -> tuple[int, int]:
        offset = 4 * channel  # registers are ON_L, ON_H, OFF_L, OFF_H
        data = self._read(6 + offset, 4)
        on_t, off_t = data[:2], data[2:]
        return (
            int.from_bytes(on_t, "little"),
            int.from_bytes(off_t, "little"),
        )

    def _frequency_from_prescale(self, prescale: int) -> int:
        return round(self.clk_hz / (4096 * (prescale + 1)))

    def frequency(self, val_hz: "int | None" = None) -> int:
        if val_hz is not None:
            prescale = round(self.clk_hz / (4096 * val_hz)) - 1
            print(prescale)
            if prescale < 3:
                raise ValueError(
                    f"Cannot set such a high frequency: {val_hz}, maximum is {self._frequency_from_prescale(3)} Hz"
                )
            if prescale > 0xFF:
                raise ValueError(
                    f"Cannot set such a low frequency: {val_hz}, minimum is {self._frequency_from_prescale(0xff)} Hz"
                )
            mode1 = self._read(0, 1)
            self._write(
                0,
                ((int.from_bytes(mode1, "little") & 0x7F) | 0x10).to_bytes(1, "little"),
            )  # put to sleep before changing freq
            self._write(0xFE, prescale.to_bytes(1, "little"))
            self._write(0, mode1)  # restore old state
            time.sleep_us(5)

        prescale = int.from_bytes(self._read(0xFE, 1), "little")
        return self._frequency_from_prescale(prescale)
