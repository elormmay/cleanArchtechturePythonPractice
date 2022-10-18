from clean_architecture.calc.calc import Calc
import pytest


def test_add_two_numbers():
    c = Calc()
    result = c.add(4, 5)
    assert result == 9


def test_add_three_numbers():
    c = Calc()
    result = c.add(1, 3, 4)
    assert result == 8


def test_add_many_numbers():
    s = range(100)
    assert Calc.add(*s) == 4950


def test_subtract_two_numbers():
    c = Calc()
    assert c.sub(4, 3) == 1


def test_multiply_two_numbers():
    c = Calc()
    assert c.multiply(6, 3) == 18


def test_multiply_many_numbers():
    c = Calc()
    s = range(1, 10)
    assert c.multiply_many(*s) == 362880


def test_divide_two_numbers():
    c = Calc()
    assert c.divide(5, 2) == 2.5


def test_division_by_zero():
    c = Calc()
    assert c.divide(5, 0) == "inf"


# testing exception
def test_multiply_by_zero_raise_exception():
    c = Calc()
    with pytest.raises(ValueError):
        c.multiply_many(3, 0)
