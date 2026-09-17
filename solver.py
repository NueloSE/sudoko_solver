#!/usr/bin/env python3
import sys

def check_row(row, number):
    if number in row:
        return False
    return True


def check_col(board, column, number):
    for i in range(9):
        if number == board[i][column]:
            return False
    return True


def check_box(board, row, column, number):
    start_row = (row // 3) * 3
    start_col = (column // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if number == board[i][j]:
                return False

    return True


def find_empty(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column

    return None


def is_valid_board(board):
    errors = []
    for row in range(9):
        seen = []
        for col in range(9):
            number = board[row][col]
            if number == 0:
                continue
            if number in seen:
                errors.append(f"Row {row + 1} has duplicate number {number}")
                break
            seen.append(number)

    # check each column for duplicates
    for col in range(9):
        seen = []
        for row in range(9):
            number = board[row][col]
            if number == 0:
                continue
            if number in seen:
                errors.append(f"Column {col + 1} has duplicate number {number}")
                break
            seen.append(number)

    # check each 3x3 box for duplicates
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            seen = []
            found_dup = False
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    number = board[i][j]
                    if number == 0:
                        continue
                    if number in seen:
                        box_num = (box_row // 3) * 3 + (box_col // 3) + 1
                        errors.append(
                            f"Box {box_num} (rows {box_row + 1}-{box_row + 3}, cols {box_col + 1}-{box_col + 3}) has duplicate number {number}"
                        )
                        found_dup = True
                        break
                    seen.append(number)
                if found_dup:
                    break

    return errors


def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True

    row, column = empty

    for number in range(1, 10):
        if (check_row(board[row], number)
                and check_col(board, column, number)
                and check_box(board, row, column, number)):

            board[row][column] = number

            if solve(board):
                return True

            board[row][column] = 0

    return False


def print_board(board):
    for row_index, row in enumerate(board):
        for column_index, number in enumerate(row):

            print(number, end=" ")

            if column_index == 2 or column_index == 5:
                print("|", end=" ")

        print()

        if row_index == 2 or row_index == 5:
            print("---------------------")


def main():
    rows = sys.argv[1:]

    # Check for exactly 9 rows
    if len(rows) == 0:
        print("\tUsage: ./solver.py row1 row2 row3 row4 row5 row6 row7 row8 row9")
        print("\tEach row must be 9 digits (0-9), use 0 for empty cells.")
        print()
        print("\t\tExample: ./solver.py 530070000 600195000 098000060 800060003 \n\t\t400803001 700020006 060000280 000419005 000080079")
        return

    if len(rows) != 9:
        print(f"Error: Expected 9 rows but got {len(rows)}.")
        return

    board = []

    # Check every row
    for row in rows:

        if len(row) != 9:
            print("Error: Each row must contain exactly 9 digits.")
            return

        if not row.isdigit():
            print("Error: Each row must contain only digits.")
            return

        board.append([int(number) for number in row])

    # Check that the starting board follows Sudoku rules
    errors = is_valid_board(board)
    if errors:
        print("Error: The Sudoku board is invalid.")
        for error in errors:
            print(f"  - {error}")
        return

    # Check whether the board can be solved
    if not solve(board):
        print("Error: This Sudoku board has no solution.")
        return

    print_board(board)


if __name__ == "__main__":
    main()

