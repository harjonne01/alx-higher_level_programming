#!/usr/bin/python3

# function that removes all characters c and C from a string.

def no_c(my_string):
    New_str = my_string.replace('c', '').replace('C', '')
    return (New_str)
