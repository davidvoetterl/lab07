import pytest

from a_open_and_closed_box_tests.python.absolute import absolute_value_of

def test_absolute_value_of_pos():
    input = 5
    output = 5
    assert absolute_value_of(input) == output

def test_absolute_value_of_neg():
    input = -8
    output = 8
    assert absolute_value_of(input) == output

def test_absolute_value_of_zer():
    input = 0
    output = 0
    assert absolute_value_of(input) == output

def test_absolute_value_of_neg1():
    input = -1
    output = 1
    assert absolute_value_of(input) == output





