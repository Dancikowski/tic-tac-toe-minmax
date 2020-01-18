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

def setMove(x, y, player):
    board[x][y] = player

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

def render(state, human_sign, computer_sign):
    chars = {
        1: computer_sign,
        -1: human_sign,
    }

    str_line = '---------------'

    for i in range(len(state)):
        for k in range(len(state[i])):
            sign = state[i][k]
            if sign == -1 or sign == 1:
                symbol = chars[sign]
                
            else:
                symbol = str(i *3 + k + 1)
            print(f'| {symbol} |', end='')
        print('\n' + str_line)   

def computerMove(human_sign, computer_sign):
    depth = len(getAvailableMoves(board))
    if depth == 0 or isGameOver(board):
        return
    move = miniMax(board, depth, COMPUTER)
    setMove(move[0], move[1], COMPUTER)

def humanMove(human_sign, computer_sign):

    depth = len(getAvailableMoves(board))
    if depth == 0 or isGameOver(board):
        return

    move = -1
    moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

    availableMoves = getAvailableMoves(board)
    render(board, human_sign, computer_sign)
    
    while move < 1 or move > 9:
        try:
            move = int(input("Please type number 1..9: "))
            coordinate = moves[move]
            if isMoveValid(coordinate, board):
                setMove(coordinate[0], coordinate[1], PLAYER)
                return
            else:
                move = -1
                print("Invalid move")
        except(KeyError, ValueError):
            print("Bad choice")    


def main():

    human_sign = ""
    computer_sign = ""
    first = ""

    while human_sign != "O" and human_sign != "X":
        
        human_sign = input("Please choose X or O: ").upper()
        if (human_sign != "O" and human_sign != "X"):
            print("Bad choice. Please choose X or O: ")
        else:
            print("You've chosen ", human_sign)

    # let human start        
    first = human_sign

    # set computer sign
    if human_sign == "O":
        computer_sign = "X"
    else:
        computer_sign = "O"   
    
    depth = len(getAvailableMoves(board))
    
    while depth and not isGameOver(board):
        humanMove(human_sign, computer_sign)
        computerMove(human_sign, computer_sign)
        depth = len(getAvailableMoves(board))

    if wins(board, PLAYER):
        print("You won!")
        render(board, human_sign, computer_sign)
        return
    if wins(board, COMPUTER):
        print("You lost!")
        render(board, human_sign, computer_sign)
    else:
        print("It's draw!")
        render(board, human_sign, computer_sign)
        return
    exit()

if __name__ == "__main__":
    main()
    