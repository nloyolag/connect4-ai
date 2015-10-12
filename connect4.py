import sys
import numpy

BOARD_SIZE_X = 7
BOARD_SIZE_Y = 6
SEARCH_DEPTH = 4

COMPUTER_PLAYER = 1
HUMAN_PLAYER = -1

def minimax(gameState, depth, player, opponent):
    availableMoves = BOARD_SIZE_X
    for i in range(0, BOARD_SIZE_X):
        if gameState[0][i] != 0:
            availableMoves -= 1

    if depth == 0 or availableMoves == 0:
        score = evaluateScore(gameState, COMPUTER_PLAYER, HUMAN_PLAYER)
        return None, score

    bestScore = None
    bestMove = None

    for i in range(0, BOARD_SIZE_X):
        if gameState[0][i] != 0:
            continue

        currentMove = [0, i]

        for j in range(0, BOARD_SIZE_Y - 1):
            if gameState[j + 1][i] != 0:
                gameState[j][i] = player
                currentMove[0] = j
                break

        move, score = minimax(gameState, depth - 1, opponent, player)

        gameState[currentMove[0]][currentMove[1]] = 0

        if player == COMPUTER_PLAYER:
            if bestScore == None or score > bestScore:
                bestScore = score
                bestMove = currentMove
        else:
            if bestScore == None or score < bestScore:
                bestScore = score
                bestMove = currentMove

    return bestMove, bestScore

def evaluateScore(gameState, player, opponent):
    score = checkWin(gameState)

    if score == player:
        return float("inf")
    elif score == opponent:
        return float("-inf")
    else:
        score = 0

    for i in range(0, BOARD_SIZE_Y):
        for j in range(0, BOARD_SIZE_X):
            if gameState[i][j] == 0:
                score += scoreOfCoordinate(gameState, i, j, player, opponent)

    return score

def scoreOfCoordinate(gameState, i, j, player, opponent):
    score = 0

    # Check vertical line
    score_temp = scoreOfLine(
                     gameState=gameState,
                     i=i,
                     j=j,
                     rowIncrement=-1,
                     columnIncrement=0,
                     firstRowCondition=-1,
                     secondRowCondition=BOARD_SIZE_Y,
                     firstColumnCondition=None,
                     secondColumnCondition=None,
                     player=player,
                     opponent=opponent
                 )

    score += score_temp

    # Check horizontal line
    score_temp = scoreOfLine(
                     gameState=gameState,
                     i=i,
                     j=j,
                     rowIncrement=0,
                     columnIncrement=-1,
                     firstRowCondition=None,
                     secondRowCondition=None,
                     firstColumnCondition=-1,
                     secondColumnCondition=BOARD_SIZE_X,
                     player=player,
                     opponent=opponent
                 )

    score += score_temp

    # Check diagonal /
    score_temp = scoreOfLine(
                     gameState=gameState,
                     i=i,
                     j=j,
                     rowIncrement=-1,
                     columnIncrement=1,
                     firstRowCondition=-1,
                     secondRowCondition=BOARD_SIZE_Y,
                     firstColumnCondition=BOARD_SIZE_X,
                     secondColumnCondition=-1,
                     player=player,
                     opponent=opponent
                 )

    score += score_temp

    # Check diagonal \
    score_temp = scoreOfLine(
                     gameState=gameState,
                     i=i,
                     j=j,
                     rowIncrement=-1,
                     columnIncrement=-1,
                     firstRowCondition=-1,
                     secondRowCondition=BOARD_SIZE_Y,
                     firstColumnCondition=-1,
                     secondColumnCondition=BOARD_SIZE_X,
                     player=player,
                     opponent=opponent
                 )

    score += score_temp

    return score

def scoreOfLine(
    gameState,
    i,
    j,
    rowIncrement,
    columnIncrement,
    firstRowCondition,
    secondRowCondition,
    firstColumnCondition,
    secondColumnCondition,
    player,
    opponent
):
    score = 0
    currentInLine = 0
    valsInARow = 0
    valsInARowPrev = 0

    row = i + rowIncrement
    column = j + columnIncrement
    firstLoop = True
    while (
        row != firstRowCondition and
        column != firstColumnCondition and
        gameState[row][column] != 0
    ):
        if firstLoop:
            currentInLine = gameState[row][column]
            firstLoop = False
        if currentInLine == gameState[row][column]:
            valsInARow += 1
        else:
            break
        row += rowIncrement
        column += columnIncrement

    row = i - rowIncrement
    column = j - columnIncrement
    firstLoop = True
    while (
        row != secondRowCondition and
        column != secondColumnCondition and
        gameState[row][column] != 0
    ):
        if firstLoop:
            firstLoop = False
            if currentInLine != gameState[row][column]:
                if valsInARow == 3 and currentInLine == player:
                    score += 1
                elif valsInARow == 3 and currentInLine == opponent:
                    score -= 1

            else:
                valsInARowPrev = valsInARow

            valsInARow = 0
            currentInLine = gameState[row][column]

        if currentInLine == gameState[row][column]:
            valsInARow += 1
        else:
            break
        row -= rowIncrement
        column -= columnIncrement

    if valsInARow + valsInARowPrev >= 3 and currentInLine == player:
        score += 1
    elif valsInARow + valsInARowPrev >= 3 and currentInLine == opponent:
        score -= 1

    return score

def bestMove(gameState, player, opponent):
    move, score = minimax(gameState, SEARCH_DEPTH, player, opponent)
    return move[1]

def checkWin(gameState):
    current = 0
    currentCount = 0

    # Check horizontal wins
    for i in range(0, BOARD_SIZE_Y):
        for j in range(0, BOARD_SIZE_X):
            if currentCount == 0:
                if gameState[i][j] != 0:
                    current = gameState[i][j]
                    currentCount += 1
            elif currentCount == 4:
                return current
            elif gameState[i][j] != current:
                if gameState[i][j] != 0:
                    current = gameState[i][j]
                    currentCount = 1
                else:
                    current = 0
                    currentCount = 0
            else:
                currentCount += 1

        if currentCount == 4:
            return current
        current = 0
        currentCount = 0

    # Check vertical wins
    for j in range(0, BOARD_SIZE_X):
        for i in range(0, BOARD_SIZE_Y):
            if currentCount == 0:
                if gameState[i][j] != 0:
                    current = gameState[i][j]
                    currentCount += 1
            elif currentCount == 4:
                return current
            elif gameState[i][j] != current:
                if gameState[i][j] != 0:
                    current = gameState[i][j]
                    currentCount = 1
                else:
                    current = 0
                    currentCount = 0
            else:
                currentCount += 1

        if currentCount == 4:
            return current
        current = 0
        currentCount = 0

    # Check diagonal wins
    np_matrix = numpy.array(gameState)
    diags = [np_matrix[::-1,:].diagonal(i) for i in range(-np_matrix.shape[0]+1,np_matrix.shape[1])]
    diags.extend(np_matrix.diagonal(i) for i in range(np_matrix.shape[1]-1,-np_matrix.shape[0],-1))
    diags_list = [n.tolist() for n in diags]

    for i in range(0, len(diags_list)):
        if len(diags_list[i]) >= 4:
            for j in range(0, len(diags_list[i])):
                if currentCount == 0:
                    if diags_list[i][j] != 0:
                        current = diags_list[i][j]
                        currentCount += 1
                elif currentCount == 4:
                    return current
                elif diags_list[i][j] != current:
                    if diags_list[i][j] != 0:
                        current = diags_list[i][j]
                        currentCount = 1
                    else:
                        current = 0
                        currentCount = 0
                else:
                    currentCount += 1

            if currentCount == 4:
                return current
            current = 0
            currentCount = 0

    return 0

def printBoard(gameState):
    for i in range(1, BOARD_SIZE_X + 1):
        sys.stdout.write(" %d " % i)

    print ""
    print "_" * (BOARD_SIZE_X * 3)
    for i in range(0, BOARD_SIZE_Y):
        for j in range(0, BOARD_SIZE_X):

            if gameState[i][j] == 1:
                sys.stdout.write("|X|")
            elif gameState[i][j] == -1:
                sys.stdout.write("|O|")
            else:
                sys.stdout.write("|-|")

        print ""

    print "_" * (BOARD_SIZE_X * 3)
    print ""


def playGame():
    gameState = [[0 for col in range(BOARD_SIZE_X)] for row in range(BOARD_SIZE_Y)]
    moveHeights = [0] * BOARD_SIZE_X
    player = COMPUTER_PLAYER
    opponent = HUMAN_PLAYER
    winner = 0
    gameOver = False
    print "========================="
    print "= WELCOME TO CONNECT 4! ="
    print "=========================\n"
    printBoard(gameState)

    while True:

        while True:
            move = int(input("What is your move? (Choose from 1 to %d)" % BOARD_SIZE_X))
            if move < 1 or move > BOARD_SIZE_X:
                print "That is not a valid move. Try again."
            elif moveHeights[move - 1] >= BOARD_SIZE_Y:
                print "The chosen column is already full. Try again."
            else:
                break

        moveHeights[move - 1] += 1
        gameState[BOARD_SIZE_Y - moveHeights[move - 1]][move - 1] = opponent
        printBoard(gameState)

        for i in range(0, BOARD_SIZE_X):
            if moveHeights[i] != BOARD_SIZE_Y:
                break
            elif i == BOARD_SIZE_X - 1:
                gameOver = True

        if gameOver:
            break

        score = checkWin(gameState)
        if score == player:
            winner = player
            break
        elif score == opponent:
            winner = opponent
            break
        else:
            score = 0

        print "Now it's the computer's turn!"
        move = bestMove(gameState, player, opponent)
        if move == None:
            break

        moveHeights[move] += 1
        gameState[BOARD_SIZE_Y - moveHeights[move]][move] = player
        printBoard(gameState)

        score = checkWin(gameState)
        if score == player:
            winner = player
            break
        elif score == opponent:
            winner = opponent
            break
        else:
            score = 0

    return winner

if __name__ == "__main__":
    playing = True
    while playing:
        winner = playGame()
        if winner == COMPUTER_PLAYER:
            print "Damn! You lost!"
        elif winner == HUMAN_PLAYER:
            print "Congratulations! You won!"
        else:
            print "The board is full. This is a draw!"

        while True:
            option = raw_input("Do you want to play again? (Y/N)")
            if option == 'Y' or option == 'y':
                break
            elif option == 'N' or option == 'n':
                playing = False
                break
            else:
                print "Please enter Y or N."
