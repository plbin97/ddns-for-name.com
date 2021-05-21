import logging
from src import getIP
from src import connectToAPI
from src import readConfig

config = readConfig.ReadConfig('./config.ini')
localRecord = None
localIP = getIP.getIP()

def searchRecordToLocalRecord():
    recordList: list = connectToAPI.getRecordList(config.getTokenName(), config.getToken(), config.getDomain())
    if recordList is None:
        return False

    for record in recordList:
        if config.getHost() + "." + config.getDomain() + "." == record['fqdn']:
            localRecord = record
            break

if localRecord is None:
    logging.info("Record not found, creating a new record")
    newRecord = {
        "domainName": config.getDomain(),
        "host": config.getHost(),
        "type": "MX",
        "answer": localIP,
    }
    if not connectToAPI.createRecord(config.getTokenName(), config.getToken(), config.getDomain(), newRecord):
        logging.error("Create record failed")
        exit(0)
    newRecordList = connectToAPI.getRecordList(config.getTokenName(), config.getToken(), config.getDomain())


"""
onlineRecord format: 
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

while True:
