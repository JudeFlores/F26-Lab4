# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: Oct 7th, 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py
list = [3,2,5,6,7,8,21,22]
def is_even(list) :
    """
    Check if the number is even
    Parameters: list
    return: evenNums
    """
    evenNums = []
    for i in list:
        if (i%2==0) :
            evenNums.append(i)
    return evenNums                  
print(is_even(list))


