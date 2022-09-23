board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
current_player = 1
player_symbols = ['#', 'X' ,'O']
winner = 0
game_over = False

def display(board):
    print(f"{board[7]}|{board[8]}|{board[9]}\n-+-+-\n{board[4]}|{board[5]}|{board[6]}\n-+-+-\n{board[1]}|{board[2]}|{board[3]}")

def valid_position(choice, board):
    if not choice.isdigit():
        return False
    choice = int(choice)
    if choice < 1 or choice > 9:
        return False
    return board[choice] == ' '
    
def get_position(player_num, board):
    choice = ''
    while not valid_position(choice, board):
        choice = input(f"Player {player_num} - Please mark a position (1-9): ")
    return int(choice)

# Display board
display(board)

# While game is not over
while not game_over:
    
    # Get input position choice
    position = get_position(current_player, board)
    
    # Assign the position
    
    game_over = True
    
    
        # Ask current player to mark a position (1-9)
        # Check the position is valid

    # Assign the position
        # Player 1 = 'X', Player 2 = 'O'

    # Display board

    # Check winner
        # Check the current row
        # Check the current column
        # If applicable
            # Check forward diagonal 
        # If applicable
            # Check back diagonal
        
    # If there is a winner
    
        # Print winner message
    
