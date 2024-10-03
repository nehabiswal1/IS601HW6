"""My Calculator Test"""
import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

def test_addition():
    """Testing the Addition Function."""
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.add(a, b) == a + b
    assert calc.history[-1] == f"{a} + {b} = {a + b}"

def test_subtraction():
    """Testing the Subtraction Function."""
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.subtract(a, b) == a - b
    assert calc.history[-1] == f"{a} - {b} = {a - b}"

def test_multiplication():
    """Testing the Multiplication Function."""
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.multiply(a, b) == a * b
    assert calc.history[-1] == f"{a} * {b} = {a * b}"

def test_division():
    """Testing the Division Function."""
    calc = Calculator()
    a = fake.random_int(min=1)  # Avoid zero to prevent division by zero
    b = fake.random_int(min=1)
    assert calc.divide(a, b) == a / b
    assert calc.history[-1] == f"{a} / {b} = {a / b}"

def test_divide_by_zero():
    """Test the Division Function if Zero is Involved."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero. Please provide a non-zero denominator."):
        calc.divide(1, 0)

def test_last_calculation():
    """Testing Last Calculations"""
    calc = Calculator()
    calc.add(5, 3)
    assert calc.last_calculation() == "5 + 3 = 8"
    calc.subtract(10, 4)
    assert calc.last_calculation() == "10 - 4 = 6"

def test_perform_operation():
    """Testing the perform_operation method."""
    calc = Calculator()

    # Test addition
    assert calc.perform_operation("5", "3", "add") == 8
    assert calc.history[-1] == "5 + 3 = 8"

    # Test subtraction
    assert calc.perform_operation("10", "2", "subtract") == 8
    assert calc.history[-1] == "10 - 2 = 8"

    # Test multiplication
    assert calc.perform_operation("4", "5", "multiply") == 20
    assert calc.history[-1] == "4 * 5 = 20"

    # Test division
    assert calc.perform_operation("20", "4", "divide") == 5
    assert calc.history[-1] == "20 / 4 = 5"

    # Test divide by zero
    assert calc.perform_operation("1", "0", "divide") == "Cannot divide by zero. Please provide a non-zero denominator."

    # Test unknown operation
    assert calc.perform_operation("9", "3", "unknown") == "Unknown operation: unknown"

    # Test invalid number input
    assert calc.perform_operation("a", "3", "add") == "Invalid number input: a or 3 is not a valid number."
    assert calc.perform_operation("5", "b", "subtract") == "Invalid number input: 5 or b is not a valid number."

