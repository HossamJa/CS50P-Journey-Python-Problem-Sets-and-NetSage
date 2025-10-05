import pytest

from twttr import shorten

def test_shorten_low():
    assert shorten('twitaouter') == 'twttr'

def test_shorten_upp():
    assert shorten('twItAOUtEr') == 'twttr'
    assert shorten('132') == '132'
    assert shorten('?,.''') == '?,.'''
