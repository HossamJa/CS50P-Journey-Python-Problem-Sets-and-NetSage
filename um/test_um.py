import pytest
from um import count

def main():
    test_count()
    test_um_first()
    test_um_inword()


def test_count():
    assert count('Um, hello, um, world') == 2
    assert count('Um') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, hello, um, world and um, and um.') == 4

def test_um_first():
    assert count('Um... I will think of it') == 1
    assert count('Um, thank you again!') == 1


def test_um_inword():
    assert count('yummy') == 0
    assert count('yum that is good') == 0
    assert count('thanks for album') == 0



