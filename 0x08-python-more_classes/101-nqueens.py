#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    """
    Recursive function to solve the N queens problem using backtracking
    """
    if row == n:
        solutions.append([[i, col] for i, col in enumerate(board[row - 1])])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def n_queens_solver(n):
    """
    Solves the N queens problem and prints all solutions
    """
    solutions = []
    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        n_queens_solver(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
