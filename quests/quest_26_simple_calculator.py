#!/usr/bin/env python3
"""Quest 26: The Simple Calculator"""


def add(num1, num2):
    """Add two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers."""
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2


def main():
    """Main program to run the calculator."""
    print("=" * 50)
    print("THE ENCHANTED CALCULATOR")
    print("=" * 50)
    print()

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return

    print()
    print("Available operations:")
    print("  - add")
    print("  - subtract")
    print("  - multiply")
    print("  - divide")
    print()

    operation = input("What operation would you like to perform? ").lower()

    print()
    print("-" * 50)

    if operation == "add":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == "subtract":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == "divide":
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print(f"Error: '{operation}' is not a valid operation!")
        print("Please choose from: add, subtract, multiply, or divide")

    print("-" * 50)
    print()


if __name__ == "__main__":
    main()
