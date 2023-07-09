from interface import controller, psu
from time import sleep
from jsonrpc import RPC

psu(True)

sleep(0.5)

controller.__enter__()
channels = controller.channels


def fade(c):
    for i in range(100):
        channels[c].percent_brightness(i / 100)
    for i in range(100, -1, -1):
        channels[c].percent_brightness(i / 100)


channels[15].percent_brightness(1)


def get_brightness(channel: int) -> int:
    return controller.channels[channel].brightness()


def set_brightness(channel: int, brightness: int) -> int:
    return controller.channels[channel].brightness(brightness)


def channel_count() -> int:
    return len(controller.channels)


rpc = RPC(
    {
        "get_brightness": get_brightness,
        "set_brightness": set_brightness,
        "channel_count": channel_count,
    }
)

# rpc serial listener
