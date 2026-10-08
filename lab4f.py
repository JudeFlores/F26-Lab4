# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Jude Flores
# Date: October 7th
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.
def get_initials(*args) :
    initials = []
    for name in args :
        initials.append(name[0])
    return initials
    
def main() :
    print(get_initials("Alice","Bob","Charlie","David"))

if __name__ == "__main__" :
    main()