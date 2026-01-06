# Tic Tac Toe: Milestone 1 Project for "The Complete Python Bootcamp"
# Author: Chris Leung
# January 2, 2026

from random import randint
from typing import List, Tuple

# Note: Uses 1-indexed arrays for intuitive board/player numbering
# Index 0 is a padding element and unused
EMPTY_GAME_BOARD = ('#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
VALID_PLAYER_SYMBOLS = ('#', 'x', 'o')  # '#' is padding and unused
# All possible winning index combinations
WINNING_COMBINATIONS = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Cols
    (1, 5, 9), (3, 5, 7)              # Diagonals
)


def clear_screen() -> None:
    """
    Clears the display to a blank screen.
    """
    print('\n'*100)


def get_next_move(player_num: int, symbol: str, board: List[str]) -> None:
    """
    Prompts the current player to input a valid move. A valid move is a number
    between 1-9 and where that board space is empty. The player symbol is then
    recorded into that board space.

    Args:
        player_num: Current player number
        symbol: Current player's symbol
        board: The current game board
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


def get_player_symbols() -> Tuple[str, str, str]:
    """
    Asks Player 1 to input their symbol, then returns a tuple of player
    symbols, where tuple index 1 and 2 contain each respective player's
    symbol. Valid player symbols are defined by the valid_symbols variable.

    Returns:
        Tuple of player symbols, e.g. ('#', 'x', 'o') or ('#', 'o', 'x')
    """

    player_1_symbol = 'undefined'

    while player_1_symbol not in VALID_PLAYER_SYMBOLS:
        player_1_symbol = input(
            (f"Player 1, please choose your symbol ({VALID_PLAYER_SYMBOLS[1]},"
                f" or {VALID_PLAYER_SYMBOLS[2]}): "))
        if (player_1_symbol != VALID_PLAYER_SYMBOLS[1] and
                player_1_symbol != VALID_PLAYER_SYMBOLS[2]):
            print(f"Sorry, '{player_1_symbol}'' is not a valid symbol.")

    player_2_symbol = (VALID_PLAYER_SYMBOLS[2] if player_1_symbol ==
                       VALID_PLAYER_SYMBOLS[1] else VALID_PLAYER_SYMBOLS[1])

    print(f"Player 1 is {player_1_symbol}, Player 2 is {player_2_symbol}")

    return ('#', player_1_symbol, player_2_symbol)


def has_player_won(board: List[str]) -> bool:
    """
    Takes a game board and checks if any player has won.

    Args:
        board: The current game board

    Returns:
        True if any player has won, False otherwise
    """

    for combo in WINNING_COMBINATIONS:
        if ((board[combo[0]] == board[combo[1]] == board[combo[2]]) and
                board[combo[0]] != ' '):
            return True

    # Neither player has won
    return False


def print_game_board(board: List[str]) -> None:
    """
    Prints the game board.

    Args:
        board: The current game board
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


def randomly_select_starting_player() -> int:
    """
    Randomly selects which player (1 or 2) goes first and announces it via
    print statement.

    Returns:
        1 or 2
    """

    starting_player = randint(1, 2)
    print(f"Player {starting_player} goes first!")
    return starting_player


def should_start_new_game() -> bool:
    """
    Asks the players if they want to start a new game. Continues to prompt
    until a valid input is received. Valid inputs are 'y' and 'n', causing
    this function to return True or False respectively.

    Returns:
        True to play again, False to end the game
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
    board = list(EMPTY_GAME_BOARD)
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
