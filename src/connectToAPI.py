import requests
from requests.auth import HTTPBasicAuth
import logging


def getRecordList(tokenName: str, token: str, domain: str) -> list or None:
    """
    :param tokenName:
    :param token:
    Token name and token from https://www.name.com/account/settings/api
    :param domain: your domain name, such as example.org
    :return:
    if error, then return None.
    if correct, return the DNS record list:
    [
        {
            "id": 123,
            "domainName": "example.org",
            "host": "xyz",
            "fqdn": "xyz.example.org.",
            "type": "MX",
            "answer": "xxx.xxx.xxx.xxx",
            "ttl": 300,
            "priority": 10
        }
    ]
    """
    r = requests.get(f"https://api.name.com/v4/domains/{domain}/records", auth=HTTPBasicAuth(tokenName, token))
    if r.status_code != 200:
        logging.error(r.text)
        return None
    return r.json()["records"]


def getRecord(tokenName: str, token: str, domain: str, recordID: int) -> dict or None:
    """
    :param tokenName:
    :param token:
    Token name and token from https://www.name.com/account/settings/api
    :param domain: your domain name, such as example.org
    :param recordID: The record ID; you can get it from getRecordList
    :return:
    if error, then return None.
    if correct, return the DNS record in dictionary:
    {
        "id": 123,
        "domainName": "example.org",
        "host": "xyz",
        "fqdn": "xyz.example.org.",
        "type": "MX",
        "answer": "xxx.xxx.xxx.xxx",
        "ttl": 300,
        "priority": 10
    }
    """
    r = requests.get(f"https://api.name.com/v4/domains/{domain}/records/{recordID}", auth=HTTPBasicAuth(tokenName, token))
    if r.status_code != 200:
        logging.error(r.text)
        return None
    return r.json()


def deleteRecord(tokenName: str, token: str, domain: str, recordID: int) -> bool:
    """
    :param tokenName:
    :param token:
    Token name and token from https://www.name.com/account/settings/api
    :param domain: your domain name, such as example.org
    :param recordID: The record ID; you can get it from getRecordList
    :return:
    if error, return false;
    if no error, then return ture
    """
    r = requests.delete(f"https://api.name.com/v4/domains/{domain}/records/{recordID}", auth=HTTPBasicAuth(tokenName, token))
    if r.status_code != 200:
        logging.error(r.text)
        return False
    return True


def updateRecord(tokenName: str, token: str, domain: str, recordID: int, newRecord: dict) -> bool:
    """
    :param tokenName:
    :param token:
    Token name and token from https://www.name.com/account/settings/api
    :param domain: your domain name, such as example.org
    :param recordID: The record ID; you can get it from getRecordList
    :param newRecord: new record, should follows the format of
    {
        "id": 123,
        "domainName": "example.org",
        "host": "xyz",
        "fqdn": "xyz.example.org.",
        "type": "MX",
        "answer": "xxx.xxx.xxx.xxx",
        "ttl": 300,
        "priority": 10
    }
    :return:
    If no error, then return true.
    If error, then return false.
    """
    r = requests.put(f"https://api.name.com/v4/domains/{domain}/records/{recordID}", auth=HTTPBasicAuth(tokenName, token), json=newRecord)
    if r.status_code != 200:
        logging.error(r.text)
        return False
    return True


def createRecord(tokenName: str, token: str, domain: str, newRecord: dict) -> bool:
    """
    :param tokenName:
    :param token:
    Token name and token from https://www.name.com/account/settings/api
    :param domain: your domain name, such as example.org
    :param newRecord: new record, should follows the format of
    {
        "domainName": "example.org",
        "host": "xyz",
        "type": "A",
        "answer": "xxx.xxx.xxx.xxx"
    }
    :return:
    If no error, then return true.
    If error, then return false.
    """
    r = requests.post(f"https://api.name.com/v4/domains/{domain}/records", auth=HTTPBasicAuth(tokenName, token), json=newRecord)

    if r.status_code != 200:
        logging.error(r.text)
        return False
    return True

