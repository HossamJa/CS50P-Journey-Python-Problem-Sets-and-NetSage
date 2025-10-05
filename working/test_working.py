import pytest
from working import convert


def main():
    test_covert()
    test_correct_format()
    test_valid_time()


def test_covert():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'

def test_correct_format():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')

def test_valid_time():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 5:60 PM')

    with pytest.raises(ValueError):
        assert convert('09:00 AM - 17:00 PM')

    with pytest.raises(ValueError):
        assert convert('12:60 to 13:00 PM')
