# Sudoku Solver

A small command-line Sudoku solver written in plain Python. You give it a 9×9 puzzle, it checks that the puzzle doesn't already break any Sudoku rules, then fills in the blanks using backtracking and prints the finished grid.

There are two ways to give it a puzzle:

- `solver.py` takes the nine rows as command-line arguments.
- `solver2.py` reads the puzzle from a text file, like the `puzzle.txt` included in this repo.

Both run the same validation and solving code. `solver2.py` doesn't have its own solver; it imports the functions from `solver.py`.

You only need Python 3. There are no packages to install.

## What's in the repo

```
sudoko_solver/
├── solver.py     # validation, solving and printing, plus the command-line entry point
├── solver2.py    # reads a puzzle from a file, then uses solver.py to solve it
├── puzzle.txt    # a sample puzzle to try
└── README.md
```

## Getting started

```bash
git clone https://github.com/NueloSE/sudoko_solver.git
cd sudoko_solver
python3 solver2.py puzzle.txt
```

This solves the sample puzzle and prints the answer.

## Writing a puzzle

A puzzle is 9 rows of 9 digits, top to bottom. Use `0` for an empty cell.

Take this puzzle:

```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

Its first row is `530070000`, its second row is `600195000`, and so on.

### Option 1: rows as arguments (`solver.py`)

Pass each row as its own argument:

```bash
python3 solver.py 530070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079
```

Output:

```
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

Both scripts are executable, so on macOS or Linux you can also run `./solver.py ...`. Running `solver.py` with no arguments prints a usage message with an example.

### Option 2: puzzle from a file (`solver2.py`)

Typing 81 digits on the command line gets old quickly, so `solver2.py` reads them from a file. Put one row on each line:

```
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

The reader removes spaces and commas and skips blank lines, so each of these rows is read the same way:

```
530070000
5 3 0 0 7 0 0 0 0
5,3,0,0,7,0,0,0,0
```

Then run it with the file name:

```bash
python3 solver2.py puzzle.txt
```

`solver2.py` prints your starting board, then the solved one:

```
Your board:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
...

Solving...
Solved!

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
...
```

## When something is wrong with the input

The input is checked before any solving happens. You'll get a short message if:

- there aren't exactly 9 rows (`Error: Expected 9 rows but got 3.`)
- a row doesn't have exactly 9 characters (`Error: Each row must contain exactly 9 digits.`)
- a row has something other than digits in it (`Error: Each row must contain only digits.`)
- the file can't be found (`Error: File 'nope.txt' not found.`)

`solver2.py` also tells you which row of the file has the problem, e.g. `Error: Row 4 has 8 digits instead of 9.`

If the format is fine but the puzzle breaks the rules (the same number twice in a row, column or 3×3 box), you get a list of every problem it found:

```
$ python3 solver.py 550070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079
Error: The Sudoku board is invalid.
  - Row 1 has duplicate number 5
  - Box 1 (rows 1-3, cols 1-3) has duplicate number 5
```

Boxes are numbered 1 to 9, left to right and top to bottom, so box 1 is the top-left one.

If the board passes all the checks but still can't be completed, the solver says so: `Error: This Sudoku board has no solution.`

## How it works

### Checking the starting board

`is_valid_board()` looks at every row, then every column, then each of the nine 3×3 boxes. It remembers which numbers it has already seen in each one and records a message when a number shows up twice. Zeros are skipped because they're empty cells. The function returns a list of messages, and an empty list means the board is fine.

Why check first? While solving, the solver only checks the numbers it places itself. It never re-checks the numbers you started with. If you skipped this step, a puzzle with a typo in it would usually just end with "no solution", and you wouldn't know which number was the problem.

### Solving with backtracking

`solve()` is a recursive function that fills the board in place:

1. `find_empty()` scans the board left to right, top to bottom, and returns the first cell containing `0`. If there isn't one, the board is full and we're done.
2. It tries the numbers 1 to 9 in that cell. A number is only allowed if `check_row()`, `check_col()` and `check_box()` all agree it isn't already in that row, column or box.
3. When a number fits, it goes into the cell and `solve()` calls itself to fill in the rest of the board.
4. If that call can't finish the board, the cell is set back to `0` and the next number is tried.
5. If none of 1 to 9 work, `solve()` returns `False`. The previous call then undoes its guess and moves on to its next number.

```
find an empty cell ──── none left? ──► solved
        │
        ▼
try 1..9 in that cell
        │
   fits the row, column and box?
     │               │
    yes              no ──► try the next number
     │
place it, solve the rest
     │
  worked? ── yes ──► solved
     │
     no ──► put 0 back, try the next number
```

When `solve()` returns `True`, the board list has been filled in with the answer, and `print_board()` prints it with lines between the boxes.

## Functions

`solver.py`

| Function | What it does |
| --- | --- |
| `check_row(row, number)` | `True` if `number` isn't already in the row |
| `check_col(board, column, number)` | `True` if `number` isn't already in the column |
| `check_box(board, row, column, number)` | `True` if `number` isn't already in the 3×3 box that contains the cell |
| `find_empty(board)` | Returns `(row, column)` of the first empty cell, or `None` if the board is full |
| `is_valid_board(board)` | Returns a list of rule violations in the starting board |
| `solve(board)` | Fills the board in place using backtracking and returns `True` or `False` |
| `print_board(board)` | Prints the board as a grid |
| `main()` | Reads the rows from the command line, validates them, solves and prints |

`solver2.py`

| Function | What it does |
| --- | --- |
| `read_board_from_file(filepath)` | Reads and cleans up the file and returns the board as a 9×9 list, or prints what's wrong and returns `None` |

Because the logic lives in plain functions, you can use it from your own Python code too. `solver2.py` does the same thing:

```python
from solver import is_valid_board, solve, print_board

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    # ... 7 more rows
]

if not is_valid_board(board) and solve(board):
    print_board(board)
```

## Limitations

- It stops at the first solution it finds. It doesn't check whether the puzzle has only one solution.
- It's plain backtracking with no shortcuts. Everyday puzzles are solved almost instantly, but puzzles designed to defeat brute-force solvers can take a lot longer.
- It only handles standard 9×9 boards.

## Why we built this

This is a learning project. Building it gave us practice with:

- writing small functions that each do one job
- working with nested lists as a 2D grid
- validating input and giving useful error messages
- recursion and backtracking
- reading command-line arguments and files
- reusing code across files with imports
