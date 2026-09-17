# Sudoku Solver

A simple Python program that validates and solves 9×9 Sudoku puzzles.

The project provides two ways to solve a Sudoku:

* **Interactive Solver (`solver.py`)** — enter the puzzle row by row.
* **Quick Solver (`solver2.py`)** — provide the entire puzzle from the command line.

The solver uses **backtracking** to automatically find a solution.

## Features

* Accepts a 9×9 Sudoku puzzle.
* Uses `0` to represent empty cells.
* Validates rows, columns, and 3×3 blocks.
* Detects duplicate numbers and reports their locations.
* Allows users to edit incorrect rows in interactive mode.
* Automatically tries numbers from `1` to `9`.
* Uses recursion and backtracking to solve the puzzle.
* Displays the Sudoku board in a readable format.
* Reports when a puzzle has no solution.

## Files

### `solver.py`

The main interactive Sudoku solver.

It:

1. Collects the Sudoku puzzle from the user.
2. Validates each row as it is entered.
3. Displays the current board.
4. Checks the completed board for errors.
5. Allows the user to correct errors.
6. Solves the puzzle using backtracking.
7. Prints the solved board.

### `solver2.py`

A quick command-line version of the solver.

It accepts the complete Sudoku puzzle as one argument, validates it, and then uses the solving functions from `solver.py`.

## How It Works

### 1. Validate the Board

The program checks:

* Rows
* Columns
* 3×3 blocks

A valid Sudoku cannot contain the same number more than once in any of these areas.

`0` represents an empty cell and is ignored during duplicate checking.

### 2. Find an Empty Cell

The solver searches the board for an empty cell containing `0`.

### 3. Try Numbers 1–9

The program automatically tries each number from `1` to `9`.

The `can_place()` function checks whether the number can be placed in the selected cell without breaking the Sudoku rules.

### 4. Backtracking

When a number can be placed, the solver places it and continues solving.

If that choice eventually leads to a dead end, the solver removes the number and tries another possibility.

This process continues until the puzzle is solved or no possible solution remains.

## Running the Interactive Solver

Make sure Python 3 is installed.

Run:

```bash
python3 solver.py
```

Then enter the nine rows when prompted.

Each row should contain 9 numbers separated by spaces.

Use `0` for empty cells.

Example:

```text
5 3 0 0 7 0 0 0 0
```

## Running the Quick Solver

The quick solver accepts all nine rows as one command-line argument, with each row separated by a comma.

Run:

```bash
python3 solver2.py "5 3 0 0 7 0 0 0 0, 6 0 0 1 9 5 0 0 0, 0 9 8 0 0 0 0 6 0, 8 0 0 0 6 0 0 0 3, 4 0 0 8 0 3 0 0 1, 7 0 0 0 2 0 0 0 6, 0 6 0 0 0 0 2 8 0, 0 0 0 4 1 9 0 0 5, 0 0 0 0 8 0 0 7 9"
```

The program will:

1. Parse the board.
2. Check that there are 9 rows.
3. Check that each row contains 9 numbers.
4. Validate the Sudoku.
5. Solve the puzzle.
6. Print the solution.

## Main Functions

### `row_correct()`

Checks a row for duplicate numbers.

### `column_correct()`

Checks a column for duplicate numbers.

### `block_correct()`

Checks a 3×3 block for duplicate numbers.

### `find_errors()`

Finds errors in the board and returns messages describing them.

### `can_place()`

Checks whether a number can safely be placed in a particular cell.

### `find_empty()`

Finds the next empty cell.

### `solve()`

Uses recursion and backtracking to solve the Sudoku puzzle.

### `print_board()`

Displays the Sudoku board in a readable grid.

### `get_row_input()`

Collects and validates a single row from the user.

### `get_board_from_user()`

Collects the complete Sudoku board and allows rows to be edited.

## Backtracking

The basic solving process is:

```text
Find an empty cell
       ↓
Try a number from 1–9
       ↓
Is it valid?
   ↓         ↓
  Yes        No
   ↓          ↓
Place it   Try next number
   ↓
Solve the rest
   ↓
Does it work?
   ↓         ↓
  Yes        No
   ↓          ↓
 Done      Undo the choice
              ↓
        Try another number
```

## Project Goal

The goal of this project is to build a simple Sudoku solver while practicing:

* Python functions
* Lists and nested lists
* Input validation
* Recursion
* Backtracking
* Command-line arguments
* Code reuse between Python files
* Problem-solving and logical thinking
