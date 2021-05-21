import pytest
from readConfig import ReadConfig


def test_createConfigObject():
    pytest.configFromFile = ReadConfig("./config.ini")


def test_getTokenName():
    tokenName = pytest.configFromFile.getTokenName()
    assert type(tokenName).__name__ == 'str'


def test_getToken():
    token = pytest.configFromFile.getToken()
    assert type(token).__name__ == 'str'


def test_getDomain():
    domain = pytest.configFromFile.getDomain()
    assert type(domain).__name__ == 'str'


def test_getHost():
    host = pytest.configFromFile.getHost()
    assert type(host).__name__ == 'str'


def test_getIntervalOfCheck():
    intervalOfCheck = pytest.configFromFile.getIntervalOfCheck()
    assert type(intervalOfCheck).__name__ == 'int'
