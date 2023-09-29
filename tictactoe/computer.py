def empty_cells(board = []):
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
    def __init__(self, team):
        self.team = team
        self.bestMove = None

    def minimax(self, board, depth, isMaximizing):
        opponent = 'O' if self.team == 'X' else 'X'
        

        if get_winner(board, self.team):
            return 1
        elif get_winner(board, opponent):
            return -1
        elif len(empty_cells(board)) == 0:
            return 0

        if isMaximizing:
            bestScore = -1000
            
            for cell in empty_cells(board):
                board[cell[0]][cell[1]] = self.team
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
        
        for cell in empty_cells(board):
            board[cell[0]][cell[1]] = self.team
            
            score = self.minimax(board, 0, False)
            
            board[cell[0]][cell[1]] = '_'
            
            if score > bestScore:
                bestScore = score
                self.bestMove = cell
                

    def make_move(self, board):
        self.find_best_move(board)
        board[self.bestMove[0]][self.bestMove[1]] = self.team
        
        return self.bestMove != None
