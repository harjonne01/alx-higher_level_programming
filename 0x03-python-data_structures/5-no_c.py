#!/usr/bin/python3

# function that removes all characters c and C from a string.

def no_c(my_string):
    New_str = ""
    for chars in my_string:
        if (chars != 'c' and chars != 'C'):
            New_str += chars
            return (New_str)
