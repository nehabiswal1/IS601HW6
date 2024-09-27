class Calculator:
    def __init__(self):
        self.history= []

    def add(self, a: float, b: float) -> float:
        """The sum of a and b."""
        result = a + b
        self.add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """The difference of a and b."""
        result = a - b
        self.add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """The product of a and b."""
        result = a * b
        self.add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """The  quotient of a and b. Raise ValueError if b is zero."""
        if b == 0:
            raise ValueError("You cannot divide by zero. Please try again!")
        result = a / b
        self.add_to_history(f"{a} / {b} = {result}")
        return result
    def add_to_history(self, operation: str) -> None:
        """Calculation History."""
        self.history.append(operation)

    def last_calculation(self) -> str:
        """Return the last calculation from history."""
        if self.history:
            return self.history[-1]
        return "No calculations yet."

