# main.py

from dotenv import load_dotenv
import os

load_dotenv()  # Loads the environment variables from the .env file

def get_environment_variable(key):
    return os.getenv(key)

if __name__ == "__main__":
    print(f"Running in {get_environment_variable('ENVIRONMENT')} environment")
    main()

class Command:
    def execute(self, *args):
        raise NotImplementedError

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

def menu():
    print("Available commands:")
    for cmd in commands.keys():
        print(cmd)

def main():
    while True:
        user_input = input("Enter command (or 'menu' for options): ")
        if user_input == "menu":
            menu()
            continue

        try:
            command_name, *args = user_input.split()
            args = list(map(float, args))
            command = commands[command_name]
            result = command.execute(*args)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

