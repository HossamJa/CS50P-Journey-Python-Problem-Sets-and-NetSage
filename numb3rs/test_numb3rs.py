import pytest
from numb3rs import validate

def test_validate():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True

def test_invalidate():
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('1.2.3') == False
    assert validate('427.0.0.1') == False
    assert validate('5.522.0.1') == False
    assert validate('5.52.522.1') == False
    assert validate('5.52.52.565') == False
