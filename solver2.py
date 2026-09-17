#!/usr/bin/env python3
import sys
from solver import is_valid_board, solve, print_board


def read_board_from_file(filepath):
    """Reads a sudoku board from a file.

    Expected file format: 9 lines, each with 9 digits.
    Spaces and commas between digits are allowed.
    Use 0 for empty cells.

    Example file contents:
        530070000
        600195000
        098000060
        800060003
        400803001
        700020006
        060000280
        000419005
        000080079
    """
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None

    # Remove empty lines and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]

    if len(lines) != 9:
        print(f"Error: Expected 9 rows in the file but found {len(lines)}.")
        return None

    board = []

    for i, line in enumerate(lines):
        # Remove spaces and commas so formats like "5 3 0 0 7 0 0 0 0" also work
        digits = line.replace(" ", "").replace(",", "")

        if len(digits) != 9:
            print(f"Error: Row {i + 1} has {len(digits)} digits instead of 9.")
            return None

        if not digits.isdigit():
            print(f"Error: Row {i + 1} contains non-digit characters.")
            return None

        board.append([int(d) for d in digits])

    return board


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./solver2.py <filename>")
        print("Reads a sudoku board from a file and solves it.")
        print()
        print("The file should have 9 lines with 9 digits each (0 for empty cells).")
        print()
        print("Example:")
        print("  ./solver2.py puzzle.txt")
        print()
        print("Where puzzle.txt contains:")
        print("  530070000")
        print("  600195000")
        print("  098000060")
        print("  800060003")
        print("  400803001")
        print("  700020006")
        print("  060000280")
        print("  000419005")
        print("  000080079")
        sys.exit(1)

    filepath = sys.argv[1]
    board = read_board_from_file(filepath)

    if board is None:
        sys.exit(1)

    print("Your board:")
    print_board(board)

    # Validate the board
    errors = is_valid_board(board)
    if errors:
        print("\nBoard has errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    # Solve the board
    print("\nSolving...")
    if solve(board):
        print("Solved!\n")
        print_board(board)
    else:
        print("No solution exists for this board.")
