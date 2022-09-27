# Helper functions

def new_board():
    return ['#'] + 9 * [' ']

def display(board):
    print("\n" * 100)
    vertical_line = "   |   |\n"
    horizontal_line = "---+---+---\n"
    values = " {mark1} | {mark2} | {mark3}\n"
    print(vertical_line + values.format(mark1=board[7],mark2=board[8],mark3=board[9]) +
        vertical_line + horizontal_line + vertical_line + values.format(mark1=board[4],mark2=board[5],mark3=board[6]) +
        vertical_line + horizontal_line +
        vertical_line + values.format(mark1=board[1],mark2=board[2],mark3=board[3]) +
        vertical_line)

def get_symbol_selection(current_player, player_symbols):
    symbol = ''
    while symbol not in ('X','O'):
        symbol = input(f"Player {current_player} - Please choose a symbol (X or O): ").upper()
    player_symbols[current_player] = symbol
    player_symbols[2 if current_player == 1 else 1] = 'O' if symbol == 'X' else 'X'

def valid_position_selection(position, board):
    if not position.isdigit():
        return False
    position = int(position)
    if position < 1 or position > 9:
        return False
    return board[position] == ' '
    
def get_position_selection(current_player, board):
    position = ''
    while not valid_position_selection(position, board):
        position = input(f"Player {current_player} - Please mark a position (1-9): ")
    return int(position)

def has_winner(board):
    # Check each row
    for row_offset in [0,3,6]:
        if(board[1+row_offset] == board[2+row_offset] == board[3+row_offset] != ' '):
            return True
    # Check each column
    for column_offset in [0,1,2]:
        if(board[1+column_offset] == board[4+column_offset] == board[7+column_offset] != ' '):
            return True
    # Check each diagonal
    if(board[1] == board[5] == board[9] != ' '):
        return True
    if(board[3] == board[5] == board[7] != ' '):
        return True
    return False

def continue_game():
    new_game = ''
    while new_game not in ('Y','N'):
        new_game = input("New game? Y or N: ").upper()
    return new_game == 'Y'

# End of helper functions

board = new_board()
current_player = 1
player_symbols = ['#'] + 2 * [' ']
total_moves = 0
max_moves = 9
game_over = False

display(board)

get_symbol_selection(current_player, player_symbols)

while not game_over:
    
    position = get_position_selection(current_player, board)
    
    board[position] = player_symbols[current_player]
    total_moves += 1

    display(board)

    if has_winner(board):
        print(f"Player {current_player} is the winner!")
        game_over = True
    elif total_moves == max_moves:
        print(f"No winner - Draw!")
        game_over = True

    if not game_over:
        current_player = 2 if current_player == 1 else 1
    elif continue_game():
        game_over = False
        board = new_board()
        current_player = 1
        total_moves = 0
        display(board)
