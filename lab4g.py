# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: October 7th, 2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.
numbers = [2,3,4,5,6,7,8,9,10]
squares = []
squares = list(map(lambda x:x**2, numbers))
print(squares)
divisible_by_2 = []
divisible_by_2 = list(filter(lambda x: x%2==0, numbers))
print(divisible_by_2)