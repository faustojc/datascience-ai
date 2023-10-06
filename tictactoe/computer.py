import random


class Computer:
    def __init__(self, team, algorithm='minimax'):
        self.team = team
        self.bestMove = [-1, -1]
        self.algorithm = algorithm
        random.seed(0)

    @staticmethod
    def empty_cells(board: list[list[str]]):
        cells = [[row, col] for row in range(1, 4) for col in range(1, 4) if board[row][col] == '_']

        return cells

    @staticmethod
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

    def brute_force(self, board):
        opponent = 'O' if self.team == 'X' else 'X'
        bestScore = -1000
        bestMove = [-1, -1]

        cells = self.empty_cells(board)
        random.shuffle(cells)

        for cell in cells:
            board[cell[0]][cell[1]] = self.team

            # Scoring system
            if self.get_winner(board, self.team):
                score = 1
            elif self.get_winner(board, opponent):
                score = -1
            elif len(self.empty_cells(board)) == 0:
                score = 0
            else:
                board[cell[0]][cell[1]] = opponent
                score = -self.brute_force(board)

            board[cell[0]][cell[1]] = '_'

            if score > bestScore:
                bestScore = score
                bestMove = cell

        self.bestMove = bestMove
        return bestScore

    def minimax(self, board, depth, isMaximizing):
        opponent = 'O' if self.team == 'X' else 'X'
        bestScore = -1000 if isMaximizing else 1000

        # Scoring system
        if self.get_winner(board, self.team):
            return 1
        elif self.get_winner(board, opponent):
            return -1
        elif len(self.empty_cells(board)) == 0:
            return 0

        shuffled_cells = self.empty_cells(board)
        random.shuffle(shuffled_cells)

        if isMaximizing:
            for cell in shuffled_cells:
                board[cell[0]][cell[1]] = self.team
                score = self.minimax(board, depth + 1, False)

                board[cell[0]][cell[1]] = '_'
                bestScore = max(score, bestScore)

            return bestScore
        else:
            for cell in shuffled_cells:
                board[cell[0]][cell[1]] = opponent
                score = self.minimax(board, depth + 1, True)

                board[cell[0]][cell[1]] = '_'
                bestScore = min(score, bestScore)

        return bestScore

    def find_best_move(self, board):
        bestScore = -1000

        for cell in self.empty_cells(board):
            board[cell[0]][cell[1]] = self.team

            score = self.minimax(board, 0, False)

            board[cell[0]][cell[1]] = '_'

            if score > bestScore:
                bestScore = score
                self.bestMove = cell

    def make_move(self, board):
        if self.algorithm.find('brute') != -1:
            self.brute_force(board)
        else:
            self.find_best_move(board)

        board[self.bestMove[0]][self.bestMove[1]] = self.team

        return self.bestMove[0] != self.bestMove[1] != -1
