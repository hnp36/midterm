"""Unit tests for the calculator module.

This file contains tests for the basic arithmetic functions:
- addition
- subtraction
- division
- multiplication
"""
import pytest
from calculator import add, subtract, division, multiplication

def test_add():
    """Test addition function"""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtraction function"""
    assert subtract(5, 2) == 3

def test_division():
    """Test division function, including divide by zero case"""
    assert division(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        division(10, 0)

def test_multiplication():
    """Test multiplication function"""
    assert multiplication(3, 4) == 12
