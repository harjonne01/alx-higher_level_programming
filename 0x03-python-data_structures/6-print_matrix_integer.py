#!/usr/bin/python3

# function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ")
            if column != row[-1]:
                print (" ", end="")

        print()
