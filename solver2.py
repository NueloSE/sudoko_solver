import sys
from solver import find_errors, solve, print_board


def parse_board(text):
	"""Parses a board string like '0 2 0 1 ..., 3 0 0 4 ..., ...' into a 2D list."""
	rows = text.split(",")

	if len(rows) != 9:
		print(f"Error: Expected 9 rows but got {len(rows)}.")
		return None

	board = []
	for i, row_text in enumerate(rows):
		parts = row_text.split()

		if len(parts) != 9:
			print(f"Error: Row {i + 1} has {len(parts)} numbers instead of 9.")
			return None

		row = []
		for part in parts:
			if not part.isdigit() or int(part) > 9:
				print(f"Error: '{part}' in row {i + 1} is not a valid number (must be 0-9).")
				return None
			row.append(int(part))

		board.append(row)

	return board


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 solver2.py \"row1, row2, row3, ..., row9\"")
		print("Example:")
		print('  python3 solver2.py "5 3 0 0 7 0 0 0 0, 6 0 0 1 9 5 0 0 0, 0 9 8 0 0 0 0 6 0, 8 0 0 0 6 0 0 0 3, 4 0 0 8 0 3 0 0 1, 7 0 0 0 2 0 0 0 6, 0 6 0 0 0 0 2 8 0, 0 0 0 4 1 9 0 0 5, 0 0 0 0 8 0 0 7 9"')
		sys.exit(1)

	board = parse_board(sys.argv[1])

	if board is None:
		sys.exit(1)

	print("Your board:")
	print_board(board)

	# validate
	errors = find_errors(board)
	if len(errors) > 0:
		print("\nBoard has errors:")
		for error in errors:
			print(f"  - {error}")
		sys.exit(1)

	# solve
	print("\nSolving...")
	if solve(board):
		print("Solved!\n")
		print_board(board)
	else:
		print("No solution exists for this board.")

