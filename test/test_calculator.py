"""My calculator"""
from calculator import add, substract

def test_addition():
    """this is addition """
    assert add(2,2) ==4

def test_substraction():
    """this is substactiontion """
    assert substract(2,2) ==0
