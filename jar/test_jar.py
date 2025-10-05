import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(5)
    assert jar.size == 8
    jar.deposit(4)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()

    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8

    jar.withdraw(5)
    assert jar.size == 3

    jar.withdraw(2)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(13)
