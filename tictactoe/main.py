from computer import Computer

board = [
    [' ', '1', '2', '3'],
    ['1', '_', '_', '_'],
    ['2', '_', '_', '_'],
    ['3', '_', '_', '_']
]
player = 'X'
movesLeft = 9


def print_board():
    for row in board:
        for col in row:
            if col.isnumeric() or col.isspace():
                print(f'  {col} ', end='')
            else:
                print(f'| {col} ', end='')
        if board[0][3] != row[3]:
            print('|', end='\n')
        else:
            print(end='\n')


def make_move(move, letter):
    try:
        if board[move[0]][move[1]] == '_':
            board[move[0]][move[1]] = letter
            return True
    except IndexError:
        return False

    return False


def winner(letter):
    # check all rows
    for row in range(1, 4):
        if board[row][1] == board[row][2] == board[row][3] == letter:
            return True

    # check all columns
    for col in range(1, 4):
        if board[1][col] == board[2][col] == board[3][col] == letter:
            return True

    # check diagonals
    if board[1][1] == board[2][2] == board[3][3] == letter:
        return letter
    if board[1][3] == board[2][2] == board[3][1] == letter:
        return True

    return False


def start():
    global player, movesLeft
    computer = Computer('O', 'brute force')

    print_board()
    print("Input format: row, col (e.g. 1,2)", end='\n\n')

    while True:
        if movesLeft <= 0:
            print('Draw!')
            break

        move = input(f'Player {player} (row, col): ')

        try:
            move = move.split(',')
            move = [int(x) for x in move]
        except:
            print('Invalid move. Try again.')
            continue

        # Player's turn
        if make_move(move, player):
            print_board()

            if winner(player):
                print(f'Player {player} wins!')
                break

            # player = 'X' if player == 'O' else 'O'
            movesLeft -= 1

            # Computer's turn
            if computer.make_move(board):
                print(f'Computer moves ({computer.bestMove[0]}, {computer.bestMove[1]})')
                print_board()

                if winner(computer.team):
                    print(f'Computer {computer.team} wins!')
                    break

                movesLeft -= 1
        else:
            print('Invalid move. Try again.')


if __name__ == '__main__':
    start()
