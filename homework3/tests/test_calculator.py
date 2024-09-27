"""My Calculator Test"""
import pytest
from calculator import Calculator

def test_addition():
    """Testing the Addition Function."""
    calc=Calculator()
    assert calc.add(62, 2) == 64
    assert calc.history[-1] == "62 + 2 = 64"

def test_subtraction():
    """Testing the Subtraction Function."""
    calc=Calculator()
    assert calc.subtract(5, 2) == 3
    assert calc.history[-1] == "5 - 2 = 3"

def test_multiplication():
    """Testing the Multiplcation Function."""
    calc=Calculator()
    assert calc.multiply(30, 42) == 1260
    assert calc.history[-1] == "30 * 42 = 1260"

def test_division():
    """Testing the Division Function."""
    calc=Calculator()
    assert calc.divide(8, 4) == 2.0 #keep it in decimal format or else this is failing
    assert calc.history[-1] == "8 / 4 = 2.0" #same thing here

def test_divide_by_zero():
    """Test the Division Function if Zero is Involved."""
    calc=Calculator()
    with pytest.raises(ValueError, match="You cannot divide by zero. Please try again!"):
        calc.divide(1, 0)

def test_last_calculation():
    """Testing Last Calculations"""
    calc=Calculator()
    calc.add(5, 3)
    assert calc.last_calculation() == "5 + 3 = 8"
    calc.subtract(10, 4)
    assert calc.last_calculation() == "10 - 4 = 6"
