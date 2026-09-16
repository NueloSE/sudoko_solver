# VALIDATORS
# ---------------------------------------------------

# checks if a row consist of unique numbers from 1 to 9
def row_correct(board, row):
	checked_list = []
	for i in board[row]:
		if i == 0:
			continue
		if i in checked_list:
			return False
		checked_list.append(i)
	
	return True

# checks if a column only consist of numbers from 1 to 9 at most once
def column_correct(board, col):
	checked_list = []
	for row in board:
		val = row[col]
		if val == 0:
			continue
		if val in checked_list:
			return False
		checked_list.append(val)
	return True

# checks if a number already exist in the board passed
def num_in_board(board, num):
	for i in board:
		if num in i: 
			return True

	return False

# checks if a 3x3 block is valid
def block_correct(board, row, col):

	block = [[0,0,0], [0,0,0], [0,0,0]]
	i = row
	while i <= (row + 2):
		j = col
		while j <= (col + 2):
			val = board[i][j]
			# print(f"i is {i} j is {j} val is {val} ")
			if val == 0:
				j += 1
				continue
			if num_in_board(block, val):
				return False
			block_row = i
			block_col = j
			while block_row > 2:
				block_row -= 3
			while block_col > 2:
				block_col -= 3
			block[block_row][block_col] = val
			# print(block)
			j += 1
		i += 1

	return True


def sudoku_grid_correct(board):
	row = 0
	is_row_correct = True
	while row < len(board):
		is_row_correct = row_correct(board, row)
		if not is_row_correct:
			break
		row += 1

	col = 0
	is_col_correct = True
	while col < len(board):
		is_col_correct = column_correct(board, col)
		if not is_col_correct:
			break
		col += 1

	row = 0
	is_block_correct = True
	while row < len(board):
		col = 0
		while col < len(board):
			is_block_correct = block_correct(board, row, col)
			if not is_block_correct:
				break
			col += 3
		if not is_block_correct:
			break
		row += 3
	
	return is_row_correct and is_col_correct and is_block_correct


# SOLVER
# ---------------------------------------------------

# checks if placing num at board[row][col] is valid
def can_place(board, row, col, num):
	# check if num is already in the row
	if num in board[row]:
		return False

	# check if num is already in the column
	for r in range(9):
		if board[r][col] == num:
			return False

	# check if num is already in the 3x3 block
	block_row = (row // 3) * 3
	block_col = (col // 3) * 3
	for i in range(block_row, block_row + 3):
		for j in range(block_col, block_col + 3):
			if board[i][j] == num:
				return False

	return True


# finds the next empty cell (value 0) on the board
def find_empty(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return (i, j)
	return None


# solves the board using backtracking
def solve(board):
	#find an empty cell
	empty = find_empty(board)

	if empty is None:
		return True

	row, col = empty

	# try numbers 1 to 9
	for num in range(1, 10):
		# check if the number can be placed here
		if can_place(board, row, col, num):
			# place the number
			board[row][col] = num

			# try to solve the rest of the board
			if solve(board):
				return True

			# if it didn't work, undo and try the next number
			board[row][col] = 0

	# no number worked, need to backtrack
	return False


# prints the board in a readable format
def print_board(board):
	for i in range(9):
		print(board[i])
		# to be improved by Zanab


if __name__ == "__main__":
	sudoku1 = [
	  [9, 0, 0, 0, 8, 0, 3, 0, 0],
	  [2, 0, 0, 2, 5, 0, 7, 0, 0],
	  [0, 2, 0, 3, 0, 0, 0, 0, 4],
	  [2, 9, 4, 0, 0, 0, 0, 0, 0],
	  [0, 0, 0, 7, 3, 0, 5, 6, 0],
	  [7, 0, 5, 0, 6, 0, 4, 0, 0],
	  [0, 0, 7, 8, 0, 3, 9, 0, 0],
	  [0, 0, 1, 0, 0, 0, 0, 0, 3],
	  [3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print("Sudoku 1 valid:", sudoku_grid_correct(sudoku1))

	sudoku2 = [
	  [2, 6, 7, 8, 3, 9, 5, 0, 4],
	  [9, 0, 3, 5, 1, 0, 6, 0, 0],
	  [0, 5, 1, 6, 0, 0, 8, 3, 9],
	  [5, 1, 9, 0, 4, 6, 3, 2, 8],
	  [8, 0, 2, 1, 0, 5, 7, 0, 6],
	  [6, 7, 4, 3, 2, 0, 0, 0, 5],
	  [0, 0, 0, 4, 5, 7, 2, 6, 3],
	  [3, 2, 0, 0, 8, 0, 0, 5, 7],
	  [7, 4, 5, 0, 0, 3, 9, 0, 1]
	]

	print("Sudoku 2 valid:", sudoku_grid_correct(sudoku2))

	if sudoku_grid_correct(sudoku2):
		print("\nSolving sudoku 2...")
		if solve(sudoku2):
			print("Solved!\n")
			print_board(sudoku2)
		else:
			print("No solution exists.")
	else:
		print("Board is invalid, cannot solve.")