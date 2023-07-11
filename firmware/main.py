import sys
from random import getrandbits
from time import sleep

from machine import UART

uart = UART(0)

from interface import controller, psu
from jsonrpc import RPC

try:
    import asyncio
except ImportError:
    import uasyncio as asyncio

from conn import auto_reconnect, do_connect, network_status

auto_reconnect()

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


REPL_SECRET = f"DROP_TO_REPL:{getrandbits(32)}"

rpc = RPC(
    {
        "get_brightness": get_brightness,
        "set_brightness": set_brightness,
        "channel_count": channel_count,
        "frequency": controller.frequency,
        "max_brightness": lambda: 4095,
        "wifi_connect": do_connect,
        "wifi_status": network_status,
        "repl": lambda: REPL_SECRET,
    }
)


reader = asyncio.StreamReader(sys.stdin)
writer = asyncio.StreamWriter(sys.stdout)


async def main():
    try:
        uart.init(460800)
        cancelled = False
        while not cancelled:
            data = (await reader.readline()).decode()
            if not data.strip():
                continue
            resp = rpc.handle_packet(data)
            if REPL_SECRET in resp:
                cancelled = True
                import json

                data = json.loads(resp)
                data["result"] = "Dropping to repl."
                resp = json.dumps(data)
            if resp:
                writer.write(resp.encode() + b"\n")
                await writer.drain()
    except Exception as e:
        print("Error", e)
    finally:
        uart.init(115200)
        print("leaving loop")


asyncio.run(main())

print("out of loop")
