#!/usr/bin/python3


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check rows above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solve the N-queens problem using backtracking
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def solve_nqueens_util(board, row, solutions):
    """
    A recursive utility function to solve N-queens problem
    """
    if row == len(board):
        # Found a solution
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur for the next row
            solve_nqueens_util(board, row + 1, solutions)

            # Backtrack and remove the queen
            board[row][col] = 0


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line arguments
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is valid
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-queens problem
    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)
