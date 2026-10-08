# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 7th, 2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

def compute(num1, num2, operator = "+"):
    """
    Calculates the result of 2 numbers with a simple operation
    Parameters: num1, num2, operator
    Return: result
    """
    if (operator=="+"):
        result = num1 + num2
    elif (operator=="-"):
            result = num1 - num2
    elif (operator=="*"):
            result = num1 * num2
    else:
            result = num1 / num2
    return result
def main():
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter an operator(+, -, *, /): ")
      print(compute(num1, num2, operator))

if __name__ == "__main__":
      main()