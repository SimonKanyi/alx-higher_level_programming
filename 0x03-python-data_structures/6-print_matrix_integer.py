#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix (list of lists): The matrix to print.

    """
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
