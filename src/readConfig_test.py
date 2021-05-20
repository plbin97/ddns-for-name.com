import pytest
from readConfig import ReadConfig


def pytest_namespace():
    return {
        'config': None
    }


def test_createConfigObject():
    pytest.config = ReadConfig("./config.ini")


def test_getTokenName():
    tokenName = pytest.config.getTokenName()
    assert tokenName == 'plbin97'
