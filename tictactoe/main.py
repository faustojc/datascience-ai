board = [
    [' ', '1', '2', '3'],
    ['1', '_', '_', '_'],
    ['2', '_', '_', '_'],
    ['3', '_', '_', '_']
]

class Computer:
    def __init__(self, team):
        self.team = team
        self.best_move = [-1, -1]


    @staticmethod
    def empty_cells(board: list[list[str]]):
        cells = [[row, col] for row in range(1, 4) for col in range(1, 4) if board[row][col] == '_']

        return cells


    def __minimax(self, board: list[list[str]], depth: int, isMaximizing: bool) -> int:
        opponent = 'O' if self.team == 'X' else 'X'
        bestScore = -1000 if isMaximizing else 1000

        # Scoring system
        if winner(self.team):
            return 1
        elif winner(opponent):
            return -1
        elif len(self.empty_cells(board)) == 0:
            return 0

        if isMaximizing:
            for cell in self.empty_cells(board):
                board[cell[0]][cell[1]] = self.team
                score = self.minimax(board, depth + 1, False)

                board[cell[0]][cell[1]] = '_'
                bestScore = max(score, bestScore)

            return bestScore
        else:
            for cell in self.empty_cells(board):
                board[cell[0]][cell[1]] = opponent
                score = self.minimax(board, depth + 1, True)

                board[cell[0]][cell[1]] = '_'
                bestScore = min(score, bestScore)

        return bestScore

    def __find_best_move(self, board: list[list[str]]) -> None:
        bestScore = -1000

        for cell in self.empty_cells(board):
            board[cell[0]][cell[1]] = self.team

            score = self.minimax(board, 0, False)

            board[cell[0]][cell[1]] = '_'

            if score > bestScore:
                bestScore = score
                self.best_move = cell

    def make_move(self, board: list[list[str]]) -> bool:
        self.find_best_move(board)

        board[self.bestMove[0]][self.bestMove[1]] = self.team

        return self.bestMove[0] != self.bestMove[1] != -1


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
    player = 'X'
    movesLeft = 9
    computer = Computer('O')

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
        except ValueError:
            print('Invalid move. Try again.')
            continue

        # Player's turn
        if make_move(move, player):
            print_board()

            if winner(player):
                print(f'Player {player} wins!')
                break

            movesLeft -= 1
        else:
            print('Invalid move. Try again.')

        # Computer's turn
        if computer.make_move(board):
            print(f'Computer moves ({computer.best_move[0]}, {computer.best_move[1]})')
            print_board()

            if winner(computer.team):
                print(f'Computer {computer.team} wins!')
                break

            movesLeft -= 1

if __name__ == '__main__':
    start()
