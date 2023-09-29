def empty_cells(board):
    cells = []
    for row in range(1, 4):
        for col in range(1, 4):
            if board[row][col] == '_':
                cells.append([row, col])
    return cells


def get_winner(board, player):
# check all rows
    for row in range(1, 4):
        if board[row][1] == board[row][2] == board[row][3] == player:
            return True

    # check all columns
    for col in range(1, 4):
        if board[1][col] == board[2][col] == board[3][col] == player:
            return True

    # check diagonals
    if board[1][1] == board[2][2] == board[3][3] == player:
        return True
    if board[1][3] == board[2][2] == board[3][1] == player:
        return True

    return False


class Computer:
    def __init__(self, player):
        self.player = player

    def minimax(self, board, depth, isMaximizing):
        if self.player == 'X':
            opponent = 'O'
        else:
            opponent = 'X'

        if get_winner(board, self.player):
            return 1
        elif get_winner(board, opponent):
            return -1
        elif len(empty_cells(board)) == 0:
            return 0

        if isMaximizing:
            bestScore = -1000
            for cell in empty_cells(board):
                board[cell[0]][cell[1]] = self.player
                score = self.minimax(board, depth + 1, False)
                board[cell[0]][cell[1]] = '_'
                bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = 1000
            for cell in empty_cells(board):
                board[cell[0]][cell[1]] = opponent
                score = self.minimax(board, depth + 1, True)
                board[cell[0]][cell[1]] = '_'
                bestScore = min(score, bestScore)
            return bestScore

    def find_best_move(self, board):
        bestScore = -1000
        bestMove = None
        for cell in empty_cells(board):
            board[cell[0]][cell[1]] = self.player
            score = self.minimax(board, 0, False)
            board[cell[0]][cell[1]] = '_'
            if score > bestScore:
                bestScore = score
                bestMove = cell
        return bestMove

    def make_move(self, board):
        move = self.find_best_move(board)
        board[move[0]][move[1]] = self.player
        return move
