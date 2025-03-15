"""Test module for calculator operations."""

from decimal import Decimal  # Standard library imports first
import pytest  # Third-party imports next

from calculator.calculation import Calculation  # Local imports last
from calculator.operation import division

# Fixtures for operands and operation
@pytest.fixture
def operand1():
    """Fixture for the first operand."""
    return Decimal("1")

@pytest.fixture
def operand2():
    """Fixture for the second operand."""
    return Decimal("0")

@pytest.fixture
def math_operation():
    """Fixture for operation function (division)."""
    return division

# Test function that uses fixtures
# The following line suppresses the "redefined-outer-name" warning for the function
# pylint: disable=redefined-outer-name
def test_perform_operations(operand1, operand2, math_operation):  # noqa: W0621
    """
    Test calculation operations with different inputs.

    Args:
        operand1 (Decimal): First operand.
        operand2 (Decimal): Second operand.
        math_operation (function): Operation to be performed.
    """
    calculation = Calculation(operand1, operand2, math_operation)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.perform()
