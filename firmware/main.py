from interface import controller, psu
from time import sleep
from jsonrpc import RPC
from machine import UART
import sys

try:
    import asyncio
except ImportError:
    import uasyncio as asyncio

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


reader = asyncio.StreamReader(sys.stdin)
writer = asyncio.StreamWriter(sys.stdout)


async def main():
    try:
        while True:
            data = (await reader.readline()).decode()
            if not data.strip():
                continue
            resp = rpc.handle_packet(data)
            if resp:
                writer.write(resp.encode() + b"\n")
                await writer.drain()
    except Exception as e:
        print("Error", e)
    finally:
        print("leaving loop")


asyncio.run(main())
