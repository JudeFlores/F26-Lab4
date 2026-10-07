# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 7th, 2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

def sum(num1, num2):
    """
    Sums up two number
    Parameters: num1, num2
    Return: sum
    """
    sum = num1 + num2
    return sum

def main():
    print(sum(int(input("Enter the first number: ")), int(input("Enter the second number: "))))

if __name__ == "__main__":
    main()
