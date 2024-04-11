def get_integer_input(prompt):
    """
    Function to prompt the user to enter an integer.

    Args:
    - prompt (str): The prompt message to display to the user.

    Returns:
    - int: The integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter an integer.")

def gcd(a, b):
    """
    Function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
    - a (int): First number
    - b (int): Second number
    
    Returns:
    - int: The greatest common divisor (GCD) of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

# Prompt the user to enter the first number
num1 = get_integer_input("Enter the first number: ")

# Prompt the user to enter the second number
num2 = get_integer_input("Enter the second number: ")

# Find and print the greatest common divisor
print("The greatest common divisor of", num1, "and", num2, "is:", gcd(num1, num2))
