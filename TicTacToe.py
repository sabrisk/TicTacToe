choice = "y"
BOARD_SIZE = 3
board = []
SPACE = " "

# Clear out board array
def clear_board():
	global board
	board = []

# Generate a new empty board of BOARD_SIZE
def generate_board(BOARD_SIZE):
	for row in range(BOARD_SIZE):
		board.append([])
		for column in range(BOARD_SIZE):
			board[row].append(SPACE)

# Returns a dict containing the number of
# X, O, and spaces in the given array
def count_cell_values(array):
	cell_counts = {
		"space_counter": 0,
		"x_counter": 0,
		"o_counter": 0,
	}
	
	arr_index = 0

	while arr_index < len(array):
		if array[arr_index] == SPACE:
				cell_counts["space_counter"] += 1
		elif array[arr_index] == "X":
			cell_counts["x_counter"] += 1
		else:
			cell_counts["o_counter"] += 1
		
		arr_index += 1

	return cell_counts

# Returns an array representing the
# column at the specified column index
def get_column(board, col_index):

	curr_row_index = 0
	column_arr = []

	while curr_row_index < BOARD_SIZE:
		column_arr.append(board[curr_row_index][col_index])
		curr_row_index += 1

	return column_arr
	
# Returns an array representing the
# row at the specified row index
def get_row(board, row_index):

	curr_col_index = 0
	row_arr = []

	while curr_col_index < BOARD_SIZE:
		row_arr.append(board[row_index][curr_col_index])
		curr_col_index += 1

	return row_arr
	
# Returns an array representing
# the forward diaganol ex: /
def get_forward_diagonal(board):
	curr_row_index = BOARD_SIZE - 1
	curr_col_index = 0
	row_arr = []

	while curr_col_index < BOARD_SIZE:
		row_arr.append(board[curr_row_index][curr_col_index])
		curr_row_index -= 1
		curr_col_index += 1

	return row_arr

# Returns an array representing
# the forward diaganol ex: \
def get_backward_diagonal(board):
	curr_row_index = 0
	curr_col_index = 0
	row_arr = []

	while curr_col_index < BOARD_SIZE:
		row_arr.append(board[curr_row_index][curr_col_index])
		curr_row_index += 1
		curr_col_index += 1

	return row_arr	


# Returns True if the row, column or diaganol
# passed as an array won. Otherwise, returns False
def is_winner(array):
		
	cell_counts = count_cell_values(array)

	if cell_counts["space_counter"] > 0 or (cell_counts["x_counter"] > 0 and cell_counts["o_counter"] > 0):
		return False
	elif cell_counts["x_counter"] == BOARD_SIZE or cell_counts["o_counter"] == BOARD_SIZE:
		return True
	else:
		return False

# Returns an integer representing the 
# winning column if one is found.
# Otherwise, returns -1 if not
def check_columns_for_win(board):
	
	curr_col_index = 0

	while curr_col_index < BOARD_SIZE:
		if is_winner(get_column(board, curr_col_index)):
			return curr_col_index
		curr_col_index += 1
	
	return -1

# Returns an integer representing the 
# winning row if one is found.
# Otherwise, returns -1 if not
def check_rows_for_win(board):
	
	curr_row_index = 0

	while curr_row_index < BOARD_SIZE:
		if is_winner(get_row(board, curr_row_index)):
			return curr_row_index
		curr_row_index += 1
	
	return -1

# Returns True if the forward diagonal is a winner ex: /
# Otherwise, returns False
def check_forward_diagonal_for_win(board):
	return is_winner(get_forward_diagonal(board))

# Returns True if the backward diagonal is a winner ex: \
# Otherwise, returns False
def check_backward_diagonal_for_win(board):
	return is_winner(get_backward_diagonal(board))

# Returns True if a player has won
# Otherwise returns False
def check_if_won(board):
	if check_columns_for_win(board) > -1:
		winning_column_index = check_columns_for_win(board)
		print("Player " + board[0][winning_column_index] + " has won in column " + str(winning_column_index + 1) + "!")
		return True

	if check_rows_for_win(board) > -1:
		winning_row_index = check_rows_for_win(board)
		print("Player " + board[winning_row_index][0] + " has won in row " + str(winning_row_index + 1) + "!")
		return True		
	
	if check_backward_diagonal_for_win(board):
		print("Player " + board[0][0] + " has won in the backward diagonal!")
		return True

	if check_forward_diagonal_for_win(board):
		print("Player " + board[BOARD_SIZE - 1][0] + " has won in the forward diagonal!")
		return True

	return False

# Builds a String representing the board
# and prints it to the terminal
def display_board(board):
	board_text = ""
	for row_index, row in enumerate(board):
		row_text = ""

		if row_index == 0:
			for col_index, column in enumerate(row):
				if col_index == 0:
					row_text += "    " + str(col_index + 1)
				else:
					row_text += "   " + str(col_index + 1) 
			row_text += "\n"

		for col_index, column in enumerate(row):
			if col_index == 0:
				row_text += "   ----" # padding left on top border
			elif col_index > 0 and col_index < len(row) - 1:
				row_text += "----"
			else:
				row_text += "---"
		row_text += "\n"

		for col_index, column in enumerate(row):
			if col_index == 0:
				row_text+= str(row_index + 1) + " |" #left border
				row_text+= " " + board[row_index][col_index] +" "
			elif col_index > 0 and col_index < len(row) - 1:
				row_text +=  "| " + board[row_index][col_index] + " "
			else:
				row_text += "| " + board[row_index][col_index]
				row_text += " |\n"

		if row_index == len(board) - 1:
			# row_text += "   -----------"

			for i in range(BOARD_SIZE):
				if i == 0:
					row_text += "   ----" # padding left on top border
				elif i > 0 and i < BOARD_SIZE - 1:
					row_text += "----"
				else:
					row_text += "---"

		board_text += row_text
		
	print(board_text)

# Gets a tuple containing a validated
# row and column that the user entered
# for their selection
def get_user_selection():
	in_bounds = False
	
	row = input("row: ")
	column = input("column: ")

	while type(row) !=  int or type(column) !=  int or in_bounds == False:

		try:
			row = int(row)
			column = int(column)
		
			if int(row) < 1 or int(row) > BOARD_SIZE or int(column) < 1 or int(column) > BOARD_SIZE:
				print("Please enter a row and column that cooresponds to the numbers on the grid!")
				in_bounds = False
				row = input("row: ")
				column = input("column: ")
			else:
				in_bounds = True

		except ValueError:
			print('Woops! Make sure you have entered numbers for both the row and column!')
			row = input("row: ")
			column = input("column: ")
		
		return (row, column)

# Returns True if the cell was set with an X or O
# Otherwise, returns False
def make_selection(user_selection, curr_player):
	row = user_selection[0]
	column = user_selection[1]
	
	if board[row-1][column-1] == " ":
		board[row-1][column-1] = curr_player
		return True
	else:
		return False

# Switches between the two players
def switch_player(curr_player):
	if curr_player == "X":
		curr_player = "O"
	else:
		curr_player = "X"

	return curr_player

# This function will loop until there is 
# a draw, or a winner was found
def play_game():
	curr_player = "X"
	turn_counter = 0
	game_won = False

	while turn_counter  < (BOARD_SIZE * BOARD_SIZE) and game_won == False:
		print("Player " + curr_player + " make your selection!")
		print("Enter the row and column")

		user_selection = get_user_selection()

		if make_selection(user_selection, curr_player):
			curr_player = switch_player(curr_player)
			turn_counter += 1
		else:
			print("This cell has already been selected by Player " + curr_player)
		
		display_board(board)
		game_won = check_if_won(board)

	if game_won == False and turn_counter  == (BOARD_SIZE * BOARD_SIZE):
		print("Draw!")
	
while choice.lower() == "y":
	clear_board()
	generate_board(BOARD_SIZE)
	display_board(board)
	play_game()

	choice = str(input("Play again? (y/n): "))
	print("")

