"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
    
def get_valid_input(prompt, type_func=float, valid_options=None):
    while True:
        value = input(prompt).strip()
        if valid_options:
            value_lower = value.lower()
            if value_lower in valid_options:
                return value_lower
            print(f"Invalid input. Choose from {valid_options}.")
        else:
            try:
                return type_func(value)
            except (ValueError, TypeError):
                print("Not a valid input.")


def main():
    print("===== Simple Calculator =====")

    num1 = get_valid_input("Enter the first number: ")
    num2 = get_valid_input("Enter the second number: ")
    operation = get_valid_input("Enter the operation (add, subtract, multiply, divide): ",
                                type_func=str,
                                valid_options=["add", "subtract", "multiply", "divide"])

    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
