import pytest
from main import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, get_environment_variable

def test_get_environment_variable():
    current_env = get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_add_command():
    command = AddCommand()
    assert command.execute(2, 3) == 5

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(5, 3) == 2

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 3) == 6

def test_divide_command():
    command = DivideCommand()
    assert command.execute(6, 3) == 2

def test_divide_by_zero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(6, 0)

