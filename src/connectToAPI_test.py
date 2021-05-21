import pytest
import connectToAPI
import readConfig


def test_getConfigurationAndTestingRecord():
    pytest.configFromFile = readConfig.ReadConfig('./config.ini')
    pytest.testRecord = {
        "domainName": pytest.configFromFile.getDomain(),
        "host": "testtesttest",
        "type": "A",
        "answer": "127.0.0.1",
    }


def test_createRecord():
    assert connectToAPI.createRecord(pytest.configFromFile.getTokenName(), pytest.configFromFile.getToken(), pytest.configFromFile.getDomain(), pytest.testRecord) is True, "Create record failed"


def test_getRecordList():
    pytest.testRecordID = None
    recordList = connectToAPI.getRecordList(pytest.configFromFile.getTokenName(), pytest.configFromFile.getToken(), pytest.configFromFile.getDomain())
    assert recordList is not None, "Cannot get record list from API"
    for record in recordList:
        if pytest.testRecord['host'] + "." + pytest.configFromFile.getDomain() + "." == record['fqdn']:
            pytest.testRecordID = record['id']
            break
    assert pytest.testRecordID is not None, "Create record failed; test record does not found. "


def test_updateRecord():
    pytest.testRecord['answer'] = '12.12.12.12'
    assert connectToAPI.updateRecord(pytest.configFromFile.getTokenName(), pytest.configFromFile.getToken(), pytest.configFromFile.getDomain(), pytest.testRecordID, pytest.testRecord) is True, "Update record failed"


def test_getRecord():
    record = connectToAPI.getRecord(pytest.configFromFile.getTokenName(), pytest.configFromFile.getToken(), pytest.configFromFile.getDomain(), pytest.testRecordID)
    assert record is not None, "Cannot get record from API"
    assert record['answer'] == '12.12.12.12'


def test_removeRecord():
    assert connectToAPI.deleteRecord(pytest.configFromFile.getTokenName(), pytest.configFromFile.getToken(), pytest.configFromFile.getDomain(), pytest.testRecordID)
