CONF_FILE = "conf.json"


def load_conf() -> dict:
    import json

    try:
        with open(CONF_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_conf(data: dict):
    import json

    with open(CONF_FILE, "w") as f:
        json.dump(data, f)


TIMEOUT_MS = 6_000


def do_connect(ssid: str, key: str) -> dict:
    from time import sleep_ms, ticks_diff, ticks_ms

    import network

    start = ticks_ms()

    sta_if = network.WLAN(network.STA_IF)
    try:
        sta_if.disconnect()
        sleep_ms(5)
    except Exception:
        pass
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, key)
        while not sta_if.isconnected() and ticks_diff(ticks_ms(), start) < TIMEOUT_MS:
            pass
    if not sta_if.isconnected():
        raise Exception("Failed to connect.")

    data = load_conf()
    data.update({"ssid": ssid, "key": key})
    save_conf(data)
    return network_status()


def network_status() -> dict:
    import network

    sta_if = network.WLAN(network.STA_IF)
    config = ((), (), (), ()) if not sta_if.isconnected() else sta_if.ifconfig()
    return dict(zip(("ip", "subnet", "gateway", "dns"), config))


def auto_reconnect():
    data = load_conf()
    ssid, key = data.get("ssid"), data.get("key")
    if ssid and key:
        try:
            do_connect(ssid, key)
        except Exception:
            pass
