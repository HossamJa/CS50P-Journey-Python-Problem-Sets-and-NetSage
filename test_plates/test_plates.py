import pytest
from plates import is_valid

def test_is_valid():
    assert is_valid('CS50') == True
    assert is_valid('HELLO') == True
    assert is_valid('CS') == True


def test_is_invalid():
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('52TI') == False
    assert is_valid('50') == False
