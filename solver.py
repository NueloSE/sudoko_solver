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


# checks the board and returns a list of error messages
def find_errors(board):
	errors = []

	# check each row
	for i in range(9):
		if not row_correct(board, i):
			errors.append(f"Row {i + 1} has duplicate numbers")

	# check each column
	for j in range(9):
		if not column_correct(board, j):
			errors.append(f"Column {j + 1} has duplicate numbers")

	# check each 3x3 block
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			if not block_correct(board, i, j):
				block_num = (i // 3) * 3 + (j // 3) + 1
				errors.append(f"Block {block_num} (rows {i+1}-{i+3}, cols {j+1}-{j+3}) has duplicate numbers")

	return errors


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
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - + - - - + - - -")
		row_str = ""
		for j in range(9):
			if j % 3 == 0 and j != 0:
				row_str += "| "
			row_str += str(board[i][j]) + " "
		print(row_str)


# INPUT
# ---------------------------------------------------

# gets a single row from the user and validates it
def get_row_input(row_num):
	while True:
		user_input = input(f"Enter row {row_num + 1} (9 numbers 0-9 separated by spaces): ")

		parts = user_input.split()

		if len(parts) != 9:
			print(f"Error: You entered {len(parts)} numbers. Please enter exactly 9.")
			continue

		# check if all parts are valid digits 0-9
		row = []
		valid = True
		for part in parts:
			if not part.isdigit() or int(part) > 9:
				print(f"Error: '{part}' is not a valid number (must be 0-9).")
				valid = False
				break
			row.append(int(part))

		if valid:
			return row


# gets the full board from the user row by row
def get_board_from_user():
	board = []
	next_row = 0

	while next_row < 9:
		row = get_row_input(next_row)
		board.append(row)
		next_row += 1

		# show the current board so far
		print("\nCurrent board:")
		print_board(board)
		print()

		if next_row == 9:
			break

		# what  next
		while True:
			choice = input("Enter 'c' to continue, or 'e' to edit a row: ").strip().lower()

			if choice == "c":
				break
			elif choice == "e":
				# ask which row to edit
				while True:
					edit_input = input("Which row to edit? (1-" + str(len(board)) + "): ").strip()
					if edit_input.isdigit() and 1 <= int(edit_input) <= len(board):
						edit_row = int(edit_input) - 1
						break
					else:
						print(f"Error: Please enter a number between 1 and {len(board)}.")

				# get the new row and replace it
				new_row = get_row_input(edit_row)
				board[edit_row] = new_row

				print("\nCurrent board:")
				print_board(board)
				print()

			else:
				print("Error: Please enter 'c' or 'e'.")

	return board


if __name__ == "__main__":
	print(f"{'*' * 35}")
	print(f"*{' ' * 8} Sudoku Solver {' ' * 10}*")
	print(f"{'*' * 35}")
	print("Enter your sudoku puzzle row by row.")
	print("Use 0 for empty cells.\n")

	board = get_board_from_user()

	# validate and let the user fix errors before solving
	while True:
		print("\nValidating board...")
		errors = find_errors(board)

		if len(errors) == 0:
			print("Board is valid!\n")
			break

		print("Board has errors:")
		for error in errors:
			print(f"  - {error}")
		print()
		print_board(board)

		# let the user edit rows until they want to re-validate
		while True:
			edit_input = input("\nWhich row to edit? (1-9, or 'q' to quit): ").strip().lower()

			if edit_input == "q":
				print("Goodbye!")
				exit()

			if not edit_input.isdigit() or not (1 <= int(edit_input) <= 9):
				print("Error: Please enter a number between 1 and 9, or 'q' to quit.")
				continue

			edit_row = int(edit_input) - 1
			new_row = get_row_input(edit_row)
			board[edit_row] = new_row

			print("\nUpdated board:")
			print_board(board)

			choice = input("\nEnter 'e' to edit another row, or 'v' to validate: ").strip().lower()
			if choice != "e":
				break  


	print("Solving...")
	if solve(board):
		print("Solved!\n")
		print_board(board)
	else:
		print("No solution exists for this board.")