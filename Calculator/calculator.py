# This program is a simple command-line calculator.

def calculator():
    """
    Prompts the user for two numbers and an operator, then
    performs the calculation and prints the result.
    """
    # Ask the user for the first number.
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Ask the user for the operator.
    operator = input("Enter an operator (+, -, *, /): ")

    # Check if the operator is valid.
    if operator not in ['+', '-', '*', '/']:
        # % - mod
        # ** - exponents 5 ** 2 = 25
        # // - int div / floor division
        # can do +=, **= etc...
        print("Invalid operator. Please use one of the following: +, -, *, /")
        return

    # Ask the user for the second number.
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Perform the calculation based on the operator.
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero.
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2

    # Print the result.
    print("WRITE", end="")
    print('Thanks for using the calculator', f"The result is: {result}")
    print(f"|{result:10}|")
    print(f"|{result:<10}|")
    print(f"|{result:<10.0f}|")


# Run the calculator function.
if __name__ == '__main__':
    calculator()
