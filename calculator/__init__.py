"""This module contains basic arithmetic operations: addition, subtraction, 
division, and multiplication."""
def add(a, b):
    """This is addition"""
    return a + b

def subtract(a, b):
    """This is subtraction"""
    return a - b

def division(a, b):
    """This is division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiplication(a, b):
    """This is multiplication"""
    return a * b
