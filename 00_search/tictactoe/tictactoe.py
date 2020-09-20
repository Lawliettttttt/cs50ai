"""
Tic Tac Toe Player
"""

import math
import copy
import random


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #If there is odd number of EMPTYs in the board, then it's X's turn.
    return X if sum([board[i].count(EMPTY) for i in range(0,3)]) %2 == 1 \
        else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #If an element of the board is EMPTY, then it's available
    return [(i,j) for i in range(0,3) for j in range(0, 3) \
            if board[i][j] == EMPTY ]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #We need to copy the original board
    #Otherwise, the original board will be affected in intermediate operations.
    copyboard = copy.deepcopy(board)
    copyboard[action[0]][action[1]] = player(board)
    return copyboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """  
    #Horizontal check
    for i in range(0, 3):
        if board[i][0] != EMPTY and \
            board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                #player(board) function gives us the next player
                #but we need the last player
                if player(board) == X:
                    return O
                else:
                   return X
    
    #Vertical check
    for i in range(0, 3):
          if board[0][i] != EMPTY and \
              board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if player(board) == X:
                    return O
                else:
                   return X
              
    #Diagonal check (upper left to lower right)
    if board[0][0] != EMPTY and \
        board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                if player(board) == X:
                    return O
                else:
                   return X
    
    #Second diagonal check (upper right to lower left)
    if board[0][2] != EMPTY and \
        board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                if player(board) == X:
                    return O
                else:
                    return X          
        
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #If there's a winner
    if winner(board) != None:
        return True
    #If it's a tie
    if sum([board[i].count(EMPTY) for i in range(0,3)]) == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
   

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    ai_player = player(board)

    #If AI is the X player, select the first action randomly.
    if board == [[EMPTY]*3]*3:
        return (random.randint(0, 2),random.randint(0, 2))

    if ai_player == X:
        value = -math.inf
        selected_action = None
        for action in actions(board):
            #AI tries to take the maximum value possible among minimizers.
            possible_max = minimizer(result(board, action))
            if possible_max > value:
                value = possible_max
                selected_action = action
    elif ai_player == O:
        value = math.inf
        selected_action = None
        for action in actions(board):
            #AI tries to take the minimum value possible among maximizers.
            possible_min = maximizer(result(board, action))
            if possible_min < value:
                value = possible_min
                selected_action = action

    return selected_action


def maximizer(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, minimizer(result(board, action)))
        
    return value
        

def minimizer(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, maximizer(result(board, action)))
        
    return value