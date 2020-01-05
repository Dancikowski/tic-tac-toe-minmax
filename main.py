#  main.py
#  ProjectNo2 for Combinatorial Algorithms Class
#
#  Created by Damian Lasecki on 5/01/2020.

# //////////////////////////////////////////////////////
# Prerequisites
# An initial borad is represented by nested arrays [[0,0,0],[0,0,0],[0,0,0]]

PLAYER = 'X'
COMPUTER = 'O'

board = [
    ['O',0,0],
    [0,0,0],
    [0,0,0]
    ]

def score(state, depth):
    if wins(state, PLAYER):
        return 10 - depth
    elif wins(state, COMPUTER):
        return depth - 10
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


def isMoveValid(move):
    if move in emptyCells:
        return True
    else:
        return False

def getNewStateAfterMove(x,y, state, player):
    _state = state

    if isMoveValid([x,y]):
        _state[x][y] = player
        return _state
    return _state


def miniMax(state, depth):
    if isGameOver(state):
        return score(state, depth)

    depth += 1
    scores = []
    moves = []

    for x, y in getAvailableMoves(state):
        stateAfterAvailableMove = getNewStateAfterMove(x, y, state, PLAYER)
        scores.append(miniMax(stateAfterAvailableMove, depth))
        moves.append([x,y])


miniMax(board, 0)