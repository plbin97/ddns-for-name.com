import configparser
import logging

config = configparser.ConfigParser()
config.read("../config.ini")


def errorDisplay(tag):
    logging.error(f"Configuration error, tag \"{tag}\" not found")
    exit(0)


"""
Configuration check
"""
if 'account' not in config:
    errorDisplay('account')

if 'domain' not in config:
    errorDisplay('domain')

if 'local' not in config:
    errorDisplay('local')

if 'tokenName' not in config['account']:
    errorDisplay('tokenName')

if 'token' not in config['account']:
    errorDisplay('token')

if 'domain' not in config['domain']:
    errorDisplay('tokenName')

if 'host' not in config['domain']:
    errorDisplay('tokenName')

if 'interval_of_check' not in config['local']:
    errorDisplay('tokenName')


def getTokenName():
    return config['account']['tokenName']


def getToken():
    return config['account']['token']


def getDomain():
    return config['domain']['domain']


def getHost():
    return config['domain']['host']


def getIntervalOfCheck():
    return config['local']['interval_of_check']
