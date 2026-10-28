from calculadora import *


def test_soma():
    result = soma(3, 4)
    assert result == 7


def test_calculadora():
    result = calculadora(1, 5, 6)
    assert result == 11