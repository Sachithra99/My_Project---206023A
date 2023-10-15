print("Hello, world!")


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers."""
    return a / b


def main():
    """Prompts the user for two numbers and then performs the desired operation on them."""

    print("Welcome to the calculator!")

    # Get the two numbers from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user for the operation they want to perform.
    operation = input("Enter the operation you want to perform (+, -, *, /): ")

    # Perform the desired operation on the two numbers.
    result = None
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation.")
        return

    # Print the result to the console.
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
