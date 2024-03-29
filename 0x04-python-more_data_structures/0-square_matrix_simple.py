#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix.

    Args:
        matrix (list): A 2-dimensional array.

    Returns:
        list: A new matrix with each value squared.

    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix

# Test the function
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
