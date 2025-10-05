import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('2/3') == 67
    assert convert('4/4') == 100


def test_guage():

    assert gauge(75) == '75%'
    assert gauge(25) == '25%'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')
    with pytest.raises(ValueError):
        convert('one/four')
        convert('5/2')
