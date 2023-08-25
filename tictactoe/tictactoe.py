#Tic Tac Toe Player
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    #Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    #Returns player who has the next turn on a board.
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    if countX <= countO:
        return X
    else:
        return O

def actions(board):
    #Returns set of all possible actions (i, j) available on the board.
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    #Returns the board that results from making move (i, j) on the board.
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid Action")
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    #Returns the winner of the game, if there is one.
    lines = (
        # Rows
        board[0], board[1], board[2],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    )
    for line in lines:
        if line.count(X) == 3:
            return X
        elif line.count(O) == 3:
            return O

    return None
    
def terminal(board):
    #Returns True if game is over, False otherwise.
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True
    
def utility(board):
    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    #Returns the optimal action for the current player on the board.
    if terminal(board):
        return None
    if player(board) == X:
        value, action = max_value(board)
    else:
        value, action = min_value(board)
    return action

def max_value(board):
    if terminal(board):
        return utility(board), None

    value = -math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        min_value_result, _ = min_value(new_board)

        if min_value_result > value:
            value = min_value_result
            best_action = action
            if value == 1:
                return value, best_action
    return value, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None

    value = math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        max_value_result, _ = max_value(new_board)

        if max_value_result < value:
            value = max_value_result
            best_action = action
            if value == -1:
                return value, best_action
    return value, best_action