board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
current_player = 1
player_symbols = ['#', 'X' ,'O']
winner = 0
game_over = False

def display(board):
    vertical_line = "   |   |\n"
    horizontal_line = "---+---+---\n"
    values = " {mark1} | {mark2} | {mark3}\n"
    print(vertical_line + values.format(mark1=board[7],mark2=board[8],mark3=board[9]) +
        vertical_line + horizontal_line + vertical_line + values.format(mark1=board[4],mark2=board[5],mark3=board[6]) +
        vertical_line + horizontal_line +
        vertical_line + values.format(mark1=board[1],mark2=board[2],mark3=board[3]) +
        vertical_line)

def valid_position(position, board):
    if not position.isdigit():
        return False
    position = int(position)
    if position < 1 or position > 9:
        return False
    return board[position] == ' '
    
def get_position(current_player, board):
    position = ''
    while not valid_position(position, board):
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

# Display board
display(board)

# While game is not over
while not game_over:
    
    # Get input position choice
    position = get_position(current_player, board)
    
    # Assign the position
    board[position] = player_symbols[current_player]

    # Display board
    display(board)

    # Check winner
    game_over = has_winner(board)

    # If there is a winner
    if game_over:
        print(f"Player {current_player} is the winner!")
    elif current_player == 1:
        current_player = 2
    else:
        current_player = 1    
