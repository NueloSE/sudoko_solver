# Sudoku Solver

A simple Python program that validates and solves 9×9 Sudoku puzzles using recursion and backtracking.

The project provides two ways to solve a Sudoku puzzle:

* **`solver.py`** — accepts the Sudoku puzzle directly through command-line arguments.
* **`solver2.py`** — reads the Sudoku puzzle from a text file and uses the solving functions from `solver.py`.

`0` represents an empty cell.

## Features

* Accepts standard 9×9 Sudoku puzzles.
* Uses `0` for empty cells.
* Validates rows, columns, and 3×3 boxes.
* Detects duplicate numbers in the starting board.
* Automatically tries numbers from `1` to `9`.
* Uses recursion and backtracking to find a solution.
* Reports when the starting board is invalid.
* Reports when a valid board has no possible solution.
* Displays the solved Sudoku in a readable format.
* Reuses solving logic between Python files.

## Project Structure

```text
sudoko_solver/
│
├── solver.py
├── solver2.py
├── puzzle.txt
└── README.md
```

### `solver.py`

`solver.py` contains the main Sudoku-solving logic.

It:

1. Receives the nine Sudoku rows from the command line.
2. Checks that exactly nine rows were provided.
3. Checks that each row contains exactly nine digits.
4. Converts the input into a list of lists of integers.
5. Validates the starting Sudoku board.
6. Solves the puzzle using recursion and backtracking.
7. Prints the solved board.

### `solver2.py`

`solver2.py` provides a file-based way to use the solver.

It:

1. Receives the name of a puzzle file.
2. Reads the nine rows from the file.
3. Validates the file format.
4. Displays the original board.
5. Validates the Sudoku board.
6. Uses the `solve()` function from `solver.py`.
7. Prints the solved board.

The file-based solver imports the main solving functions from `solver.py`, allowing both programs to use the same Sudoku logic.

### `puzzle.txt`

`puzzle.txt` stores a Sudoku puzzle that can be passed to `solver2.py`.

Example:

```text
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

Each line represents one row of the Sudoku board.

## How It Works

### 1. Receive the Puzzle

The program first receives the Sudoku board.

For `solver.py`, the rows are provided through command-line arguments:

```bash
python3 solver.py 530070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079
```

For `solver2.py`, the puzzle is stored in a file:

```bash
python3 solver2.py puzzle.txt
```

### 2. Validate the Board

Before solving, the program checks the starting board.

It checks:

* Every row
* Every column
* Every 3×3 box

A Sudoku board cannot contain the same non-zero number more than once in any row, column, or 3×3 box.

`0` represents an empty cell and is ignored during duplicate checking.

### 3. Find an Empty Cell

The `find_empty()` function searches the board from top to bottom and left to right.

When it finds a cell containing `0`, it returns its row and column.

If there are no empty cells, the puzzle is complete.

### 4. Try Numbers 1–9

Once an empty cell is found, the solver automatically tries each number from `1` to `9`.

For each number, it checks:

* Is the number already in the row?
* Is the number already in the column?
* Is the number already in the 3×3 box?

Only a number that passes all three checks is placed in the cell.

### 5. Recursion and Backtracking

After placing a valid number, `solve()` calls itself to solve the rest of the board.

If the choice eventually leads to a situation where no number works, the program goes back to the previous choice.

It removes the number and tries another possibility.

This is called **backtracking**.

```text
Find an empty cell
        ↓
Try numbers 1–9
        ↓
Does the number fit?
     ↙       ↘
   No         Yes
   ↓           ↓
Try next    Place number
number          ↓
             Solve rest
                ↓
          Does it work?
           ↙       ↘
         No         Yes
         ↓           ↓
       Undo        Solved
       choice
         ↓
    Try another
      number
```

## Main Functions

### `check_row(row, number)`

Checks whether a number already exists in a particular row.

### `check_col(board, column, number)`

Checks whether a number already exists in a particular column.

### `check_box(board, row, column, number)`

Checks whether a number already exists in the 3×3 box containing the specified cell.

### `is_valid_board(board)`

Checks the entire starting board for duplicate numbers in rows, columns, and 3×3 boxes.

It returns a list of error messages if problems are found.

### `find_empty(board)`

Finds the next empty cell containing `0`.

It returns the row and column of the empty cell.

If no empty cells remain, it returns `None`.

### `solve(board)`

The main solving function.

It:

1. Finds an empty cell.
2. Tries numbers from `1` to `9`.
3. Checks whether each number can be placed.
4. Places a valid number.
5. Recursively continues solving.
6. Undoes the choice if it leads to a dead end.

### `print_board(board)`

Displays the Sudoku board in a readable 9×9 grid with 3×3 box separators.

## Running the Solver

### Using `solver.py`

Run:

```bash
python3 solver.py 530070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079
```

The program validates and solves the puzzle, then prints the completed board.

### Using `solver2.py`

Place the Sudoku puzzle inside a text file such as `puzzle.txt`.

Then run:

```bash
python3 solver2.py puzzle.txt
```

The program will display the original board, validate it, solve it, and display the solution.

## Example Puzzle

```text
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

`0` represents an empty cell.

## Project Goal

The goal of this project is to build a simple Sudoku solver while practicing:

* Python functions
* Lists and nested lists
* Command-line arguments
* File handling
* Input validation
* Recursion
* Backtracking
* Problem-solving
* Code reuse between Python files

The project is intentionally kept simple so that the solving process can be understood step by step rather than hidden behind complex libraries or advanced techniques.
