#  main.py
#  ProjectNo2 for Combinatorial Algorithms Class
#
#  Created by Damian Lasecki on 5/01/2020.
#
#
# Prerequisites
# An initial borad is represented by nested arrays [[0,0,0],[0,0,0],[0,0,0]]

PLAYER = -1
COMPUTER = 1

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def getScore(state, depth):
    if wins(state, PLAYER):
        return -1
    elif wins(state, COMPUTER):
        return 1
    else:
        return 0

def wins(state, player):
    
    win_states = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]

    if [player, player, player] in win_states:
        return True
    else:
        return False

    

def isGameOver(state):
    return wins(state, PLAYER) or wins(state, COMPUTER)

def getAvailableMoves(state):
    availableCells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if state[x][y] == 0:
                availableCells.append([x, y])
    
    return availableCells


def isMoveValid(move, state):
    availableCells = getAvailableMoves(state)
    if move in availableCells:
        return True
    else:
        return False

def getNewStateAfterMove(x,y, state, player):
    _state = state

    if isMoveValid([x,y], state):
        _state[x][y] = player
        return _state
    return _state

def miniMax(state, depth, player):
    if player == COMPUTER:
        best = [None, None, -float("inf")]
    else: 
        best = [None, None, float("inf")]

    if depth == 0 or isGameOver(state):
      
        score = getScore(state, depth)
        return [None, None, score]

    for x,y in getAvailableMoves(state):
        state[x][y] = player
        score = miniMax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y
        if player == COMPUTER:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

depth = len(getAvailableMoves(board))

result = miniMax(board, depth, COMPUTER)
print result