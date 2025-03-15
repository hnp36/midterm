"""Test module for calculation operations and functionality."""
import pytest
from calculator.calculation import Calculation



def test_perform_operations(value1, value2, operation, expected_result):
    """Test calculation operations with different inputs."""
    calculation = Calculation(value1, value2, operation)

    if expected_result == "ZeroDivisionError":
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculation.perform()
    else:
        assert calculation.perform() == expected_result
