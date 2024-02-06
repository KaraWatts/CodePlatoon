

# Create a Tic Tac Toe Terminal game in python
# by using prompt engineering concepts
# to generate a series of prompts that will allow you to accomplish this task.


# Features:

# Computer AI:
# - Dumb computer: prescripted move - MVP
# - smart computer: analyses board for best move - EXTRA

# Build a board:
# - show the current state of the game

# Game Flow:
# - Prompt player for move
# - Player A picks a box
# - trigger computer player response
# - Player B picks a box

# Human Player Info:
# - show the board to see curret status

import random

# Define the constants
X = 'X'
O = 'O'
EMPTY = ' '

# Create an empty nested list with 3 mutable lists filled with EMPTY
Board = [[EMPTY] * 3 for _ in range(3)]

# Function to check if coordinates are within the board range
def is_valid_coordinates(row, column):
    return 0 <= row < 3 and 0 <= column < 3

# Function to check if the board is full
def is_board_full():
    return all(EMPTY not in row for row in Board)

# Function to check if the game is won
def is_game_won():
    # Check rows
    for row in Board:
        if all(cell == X for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(Board[row][col] == X for row in range(3)):
            return True

    # Check diagonals
    if all(Board[i][i] == X for i in range(3)) or all(Board[i][i] == X for i in range(3)):
        return True

    return False

# Function to print the board
def print_board():
    for i in range(3):
        print('|'.join(Board[i]))
        if i < 2:
            print('-----')

# Main function to run the Tic-Tac-Toe game
def play_tic_tac_toe():
    # Iterate until each row has 'X' or 'O' assigned to all 3 variable spaces or game is won
    while not is_board_full() and not is_game_won():
        # Print the current board
        print_board()

        # Prompt the user for row and column inputs
        row = int(input("Where do you want to place your X?\nRow: ")) - 1
        column = int(input("Column: ")) - 1

        # Check if the coordinates are within the board range
        if not is_valid_coordinates(row, column):
            print("Invalid coordinates. Please choose coordinates within the 3x3 board.")
            continue

        # Check if the cell is already occupied
        if Board[row][column] != EMPTY:
            print("Cell already occupied. Try again.")
            continue

        # Assign X variable within the board list at [row][column]
        Board[row][column] = X

        # Check if the game is won after X's move
        if is_game_won():
            break

        # Check if the board is full after X's move
        if is_board_full():
            print_board()
            print("Cat's Game!")
            return

        # Generate random row and column for O's move
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)

        # Check if the random position is already occupied
        while Board[random_row][random_column] != EMPTY:
            random_row = random.randint(0, 2)
            random_column = random.randint(0, 2)

        # Assign O variable within the board list at [random_row][random_column]
        Board[random_row][random_column] = O

    # Print the final board when the game ends
    print_board()

    # Check the final result and print the corresponding message
    if is_game_won():
        print("You win!")
    else:
        print("You lost...try again!")


# Run the Tic-Tac-Toe game
if __name__ == "__main__":
    play_tic_tac_toe()
