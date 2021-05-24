import requests
import logging


def getIP() -> str or None:
    r = requests.get("https://api.ipify.org")
    if r.status_code == 200:
        return r.text
    backUpRequest = requests.get("https://httpbin.org/ip")
    if backUpRequest.status_code == 200:
        return backUpRequest.json()['origin']
    return None
