import logging

from src import connectToAPI
from src import readConfig
import ipify

recordList: list = connectToAPI.getRecordList(readConfig.getTokenName(), readConfig.getToken(), readConfig.getDomain())
if recordList is None:
    exit(0)

onlineRecord = None
for record in recordList:
    if readConfig.getHost() + "." + readConfig.getDomain() + "." == record['fqdn']:
        onlineRecord = record
        break

if onlineRecord is None:
    logging.info("Record not found")
    newRecord = {
        "domainName": readConfig.getDomain(),
        "host": readConfig.getHost(),
        "type": "MX",
        "answer": ipify.get_ip(),
    }
    if not connectToAPI.createRecord(readConfig.getTokenName(), readConfig.getToken(), readConfig.getDomain(), newRecord):
        logging.error("Create record failed")
        exit(0)
 
#
# # print(connectToAPI.getRecordList("plbin97", "fb8f398a9179193e330f6e8b262ff3d2b2efbd41", "teenet.me"))
# data = {
#     'id': 195929576,
#     'domainName': 'teenet.me',
#     'host': 'home',
#     'fqdn': 'home.teenet.me.',
#     'type': 'A',
#     'answer': '13.13.13.13',
#     'ttl': 300
# }
# print(connectToAPI.updateRecord("plbin97", "fb8f398a9179193e330f6e8b262ff3d2b2efbd41", "teenet.me", 195929576, data))
# print()
