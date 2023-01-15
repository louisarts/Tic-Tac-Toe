# Tic-Tac-Toe game simulation

# Initialize the game board as a list of 9 empty spaces
board = [" " for x in range(9)]

# Function to print the current state of the game board
def print_board():
    # Create a string representation of each row of the board
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    # Print the board
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle a player's move
def player_move(icon):
    # Determine which player's turn it is
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    # Prompt the player to make a move
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    # Update the game board if the chosen space is empty
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

# Function to check for a winning condition
def is_victory(icon):
    # Check for a win along rows, columns, and diagonals
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Function to check for a draw
def is_draw():
    if " " not in board:
        return True
    else:
        return False

# Main game loop
while True:
    # Print the current state of the board
    print_board()
    # Player X makes a move
    player_move("X")
    # Print the current state of the board
    print_board()
    # Check for a win or a draw
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    # Player O makes a move
    player_move("O")
   
