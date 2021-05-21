import pytest
import getIP


def test_getIP():
    assert getIP.getIP() is not None
