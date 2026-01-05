# Tic Tac Toe: Milestone 1 Project for "The Complete Python Bootcamp"
# Author: Chris Leung
# January 2, 2026

from random import randint

EMPTY_GAME_BOARD = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def clear_screen():
    """
    Clears the display to a blank screen.
    """
    print('\n'*100)


def get_next_move(player_num, symbol, board):
    """
    Prompts the current player to input a valid move. A valid move is a number
    between 1-9 and where that board space is empty. The player symbol is then
    recorded into that board space.

    Args:
        player_num (int): Current player number
        symbol (str): Current player's symbol
        board (list): The current game board
    """

    valid_move = False
    while not valid_move:
        user_input = input(
            f"Player {player_num}, please enter your move (1-9): ")

        # Check whether inputted move is valid
        if user_input.isdigit():
            selected_space = int(user_input)
            if (selected_space >= 1 and selected_space <= 9 and
                    board[selected_space] == ' '):
                valid_move = True
                board[selected_space] = symbol

        if not valid_move:
            print(f"Sorry, '{user_input}' is not a valid move.")


def get_player_symbols():
    """
    Asks Player 1 to input their symbol, then returns a tuple of player
    symbols, where tuple index 1 and 2 contain each respective player's
    symbol. Valid player symbols are defined by the valid_symbols variable.

    Returns:
        tup: e.g. ('#', 'x', 'o') or ('#', 'o', 'x')
    """

    VALID_SYMBOLS = ['', 'x', 'o']

    player_1_symbol = 'undefined'

    while player_1_symbol not in VALID_SYMBOLS:
        player_1_symbol = input(
            (f"Player 1, please choose your symbol ({VALID_SYMBOLS[1]}, or "
                f"{VALID_SYMBOLS[2]}): "))
        if (player_1_symbol != VALID_SYMBOLS[1] and
                player_1_symbol != VALID_SYMBOLS[2]):
            print(f"Sorry, '{player_1_symbol}'' is not a valid symbol.")

    if player_1_symbol == VALID_SYMBOLS[1]:
        chosen_symbols = tuple(['', VALID_SYMBOLS[1], VALID_SYMBOLS[2]])
    else:
        chosen_symbols = tuple(['', VALID_SYMBOLS[2], VALID_SYMBOLS[1]])

    print(f"Player 1 is {chosen_symbols[1]}, Player 2 is {chosen_symbols[2]}")

    return chosen_symbols


def has_player_won(board):
    """
    Takes a game board and checks if any player has won.

    Args:
        board (list): The current game board

    Returns:
        bool: True if any player has won, False otherwise
    """

    # Check each row
    for row in range(0, 7, 3):
        if (board[1+row] != ' ' and
                (board[1+row] == board[2+row] == board[3+row])):
            return True
    # Check each column
    for col in range(0, 3):
        if (board[1+col] != ' ' and
                (board[1+col] == board[4+col] == board[7+col])):
            return True
    # Check diagonals
    if (board[5] != ' ' and
        ((board[1] == board[5] == board[9])
            or (board[3] == board[5] == board[7]))):
        return True

    # Neither player has won
    return False


def print_game_board(board):
    """
    Prints the game board.

    Args:
        board (list): The current game board
    """

    board_output = (
        "   |   |   \n"
        f" {board[1]} | {board[2]} | {board[3]}\n"
        "   |   |   \n"
        "---+---+---\n"
        "   |   |   \n"
        f" {board[4]} | {board[5]} | {board[6]}\n"
        "   |   |   \n"
        "---+---+---\n"
        "   |   |   \n"
        f" {board[7]} | {board[8]} | {board[9]}\n"
        "   |   |   \n")
    clear_screen()
    print(board_output)


def randomly_select_starting_player():
    """
    Randomly selects which player (1 or 2) goes first and announces it via
    print statement.

    Returns:
        int: 1 or 2
    """

    starting_player = randint(1, 2)
    print(f"Player {starting_player} goes first!")
    return starting_player


def should_start_new_game():
    """
    Asks the players if they want to start a new game. Continues to prompt
    until a valid input is received. Valid inputs are 'y' and 'n', causing
    this function to return True or False respectively.

    Returns:
        bool: True to play again, False to end the game
    """

    while True:
        response = input("Would you like to start a new game? (y/n): ")
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print(f"Sorry, '{response}' is not a valid input.")


# Show welcome message
clear_screen()
print("Welcome to Tic Tac Toe!")

while True:
    # Game setup
    game_over = False
    board = EMPTY_GAME_BOARD.copy()
    num_moves_made = 0
    player_symbols = get_player_symbols()

    # Start the game
    print_game_board(board)
    current_player = randomly_select_starting_player()
    while not game_over:

        get_next_move(current_player,
                      player_symbols[current_player], board)
        num_moves_made += 1

        print_game_board(board)

        if has_player_won(board):
            print(f"Game over - Player {current_player} wins!")
            game_over = True
        elif num_moves_made == 9:  # Board is full
            print("Game over - Stalemate!")
            game_over = True

        if not game_over:
            # Switch players
            current_player = 1 if current_player == 2 else 2

    if not should_start_new_game():
        break

print("Thanks for playing! Goodbye!")
