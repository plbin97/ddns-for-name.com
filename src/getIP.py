import requests
import logging

def getIP():
    r = requests.get("https://api.ipify.org")
    if r.status_code != 200:
        return None
    return r.text