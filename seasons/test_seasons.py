import pytest
from seasons import get_date

def main():
    test_get_date()
    test_correct_format()

def test_get_date():
    assert get_date('1999-01-01') == 'Thirteen million, seven hundred sixty-four thousand, nine hundred sixty minutes'


def test_correct_format():
    with pytest.raises(SystemExit):
        assert get_date('January 1, 1999')
