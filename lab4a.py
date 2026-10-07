# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: Oct 7th, 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py
list = [1, 3, 5, 7, 9, 11, 13]
def is_even(list) :
    """
    Check if the number is even
    Parameters: list
    return: isEven
    """
    isEven = False
    for i in list:
        if (i%2==0) :
            isEven = True
            break
    return isEven       

print(is_even(list))


