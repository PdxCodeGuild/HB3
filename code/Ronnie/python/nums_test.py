import pytest
from nums_to_words import nums_to_words

def test_dynamic():
    assert nums_to_words(34) == 'thirty-four'

def test_static():
    assert nums_to_words(30) == 'thirty'

def test_single():
    assert nums_to_words(5) == 'five'