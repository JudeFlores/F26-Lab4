# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 7th, 2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py
def even_numbers(list):
    """
    Gets a list and gives back a list of the even numbers
    Parameters: list
    Return: evenNums
    """
    evenNums = []
    for i in list:
        if(i%2==0):
            evenNums.append(i)
    return(evenNums)
list = [1,1,1,1,1,1,1,1,1]
print(even_numbers(list))

