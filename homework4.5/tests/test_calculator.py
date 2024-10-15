# tests/test_calculator.py

import unittest
from main import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCalculatorCommands(unittest.TestCase):
    def test_add(self):
        command = AddCommand()
        self.assertEqual(command.execute(1, 2), 3)

    def test_subtract(self):
        command = SubtractCommand()
        self.assertEqual(command.execute(5, 3), 2)

    def test_multiply(self):
        command = MultiplyCommand()
        self.assertEqual(command.execute(3, 4), 12)

    def test_divide(self):
        command = DivideCommand()
        self.assertEqual(command.execute(10, 2), 5)
        with self.assertRaises(ValueError):
            command.execute(10, 0)

if __name__ == "__main__":
    unittest.main()

