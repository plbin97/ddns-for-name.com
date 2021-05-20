import configparser
import logging
from os import path


def errorDisplay(tag):
    logging.error(f"Configuration error, tag \"{tag}\" not found")
    exit(0)


class ReadConfig:

    def __init__(self, configFile):
        if not path.exists(configFile):
            raise Exception("Configuration file does not exist")

        self.config = configparser.ConfigParser()
        self.config.read(configFile)

        """
        Configuration check
        """
        if 'account' not in self.config:
            errorDisplay('account')

        if 'domain' not in self.config:
            errorDisplay('domain')

        if 'local' not in self.config:
            errorDisplay('local')

        if 'tokenName' not in self.config['account']:
            errorDisplay('tokenName')

        if 'token' not in self.config['account']:
            errorDisplay('token')

        if 'domain' not in self.config['domain']:
            errorDisplay('tokenName')

        if 'host' not in self.config['domain']:
            errorDisplay('tokenName')

        if 'interval_of_check' not in self.config['local']:
            errorDisplay('tokenName')

    def getTokenName(self):
        return self.config['account']['tokenName']

    def getToken(self):
        return self.config['account']['token']

    def getDomain(self):
        return self.config['domain']['domain']

    def getHost(self):
        return self.config['domain']['host']

    def getIntervalOfCheck(self):
        return self.config['local']['interval_of_check']
