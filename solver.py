# Write your solution here
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
	
	checked_board = []

	for rows in board:
		i = 0
		while i < 9:
			if i != col or rows[i] == 0:
				i += 1
				continue
			if rows[i] in checked_board:
				return False
			checked_board.append(rows[i])
			i += 1
	
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

	print(sudoku_grid_correct(sudoku1))

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

	print(sudoku_grid_correct(sudoku2))

	sudoku3 = [
	  [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
	  [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
	  [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
	  [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
	  [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
	  [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
	  [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
	  [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
	  [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
	]
	print(sudoku_grid_correct(sudoku3))