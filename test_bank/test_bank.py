import pytest
from bank import value

def test_value_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
def test_value_h():
    assert value("Hey") == 20
    assert value("How you doing?") == 20
def test_value_other():
    assert value("greetings") == 100
    assert value("What's happening?") == 100
