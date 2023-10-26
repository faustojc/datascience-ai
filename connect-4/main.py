board = [
    [' ', '1', '2', '3', '4', '5', '6', '7'],
    [' ', '_', '_', '_', '_', '_', '_', '_'],
    [' ', '_', '_', '_', '_', '_', '_', '_'],
    [' ', '_', '_', '_', '_', '_', '_', '_'],
    [' ', '_', '_', '_', '_', '_', '_', '_'],
    [' ', '_', '_', '_', '_', '_', '_', '_'],
    [' ', '_', '_', '_', '_', '_', '_', '_']
]
player = 'X'
movesLeft = 42

def print_board():
    for row in board:
        for col in row:
            if col.isnumeric() or col.isspace():
                print(f'  {col} ', end='')
            else:
                print(f'| {col} ', end='')
        if board[0][7] != row[7]:
            print('|', end='\n')
        else:
            print(end='\n')

def make_move(move, letter):
    for row in range(6, 0, -1):
        if board[1][move] != '_':
            print('Column Occupied!')
            return False
        
        if board[row][move] == '_':
            board[row][move] = letter
            return True
        
    return False

def winner(letter):
    # check all rows
    for row in range(1, 7):
        for col in range(1, 5):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == letter:
                return True

    # check all columns
    for col in range(1, 8):
        for row in range(1, 4):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == letter:
                return True

    # check diagonals
    for row in range(1, 4):
        for col in range(1, 5):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == letter:
                return True
            if board[row][col+3] == board[row+1][col+2] == board[row+2][col+1] == board[row+3][col] == letter:
                return True

    return False

def start():
    global player, movesLeft

    print_board()

    while True:
        if movesLeft <= 0:
            print('Draw!')
            break

        try:
            move = int(input(f'Player {player} col (1 to 7): '))
            
            if (move <= 0 and move >= 8):
                print('Invalid move!')
                continue   
            
            # Player's turn
            if make_move(move, player):
                print_board()

                if winner(player):
                    print(f'Player {player} wins!')
                    break

                player = 'X' if player == 'O' else 'O'
                movesLeft -= 1
        except:
            print('Invalid input!')      
            

if __name__ == '__main__':
    start()
