#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """
    Recursive function to solve the N queens problem using backtracking
    """
    if col >= n:
        print_solution(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1, n) or res
            board[i][col] = 0  # backtrack if placing a queen at board[i][col] doesn't lead to a solution
    return res

def print_solution(board, n):
    """
    Print the board configuration as a solution
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def n_queens_solver(n):
    """
    Solves the N queens problem and prints all solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        n_queens_solver(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
