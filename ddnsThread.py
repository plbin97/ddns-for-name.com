import logging
import time

from src import getIP
from src import connectToAPI
from src import readConfig


def run():
    config = readConfig.ReadConfig('./config.ini')
    localRecord: dict


    def searchRecordToLocalRecord() -> bool:
        """
        Search online record via API, and write the record into 'localRecord' variable
        :return:
        return true if record founded.
        return false if record not founded or error.
        """
        recordList: list = connectToAPI.getRecordList(config.getTokenName(), config.getToken(), config.getDomain())
        if recordList is None:
            return False
        for record in recordList:
            if config.getHost() + "." + config.getDomain() + "." == record['fqdn']:
                global localRecord
                localRecord = record
                return True
        return False


    if not searchRecordToLocalRecord():
        print("Record not found, creating a new record")
        localIP = getIP.getIP()
        while localIP is None:
            logging.error("Get IP failed, retrying")
            localIP = getIP.getIP()

        newRecord = {
            "domainName": config.getDomain(),
            "host": config.getHost(),
            "type": "A",
            "answer": getIP.getIP(),
        }
        if not connectToAPI.createRecord(config.getTokenName(), config.getToken(), config.getDomain(), newRecord):
            logging.error("Create record failed")
            exit(0)
        if not searchRecordToLocalRecord():
            logging.error("Create record failed; created but not on the list")
            exit(0)
        print("Create record success")

    """
    localRecord format: 
    {
        "id": 123,
        "domainName": "example.org",
        "host": "www",
        "fqdn": "www.example.org.",
        "type": "A",
        "answer": "127.0.0.1",
        "ttl": 300
    }
    """

    print("start watching")
    while True:

        localIP = getIP.getIP()
        while localIP is None:
            logging.error("Get IP failed, retrying")
            localIP = getIP.getIP()

        if localIP != localRecord['answer']:
            print(f"IP changed from {localRecord['answer']} to {localIP}")
            localRecord['answer'] = localIP
            connectToAPI.updateRecord(config.getTokenName(), config.getToken(), config.getDomain(), localRecord['id'], localRecord)

        time.sleep(config.getIntervalOfCheck())
