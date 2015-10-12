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

        for j in range(1, BOARD_SIZE_Y):
            if gameState[j][i] != 0:
                gameState[j-1][i] = player
                moveLocation[0] = j - 1
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
    score = 0

    for i in range(0, BOARD_SIZE_X):
        for j in range(0, BOARD_SIZE_Y):
            if gameState[j][i] == 0:
                score_temp = scoreOfCoordinate(gameState, i, j, player, opponent)

                if score_temp == float("inf") or score_temp == float("-inf"):
                    return score_temp
                else:
                    score += score_temp

    return score

def bestMove(gameState, player, opponent):
    move, score = minimax(gameState, SEARCH_DEPTH, player, opponent)
    return move

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
    if score_temp == float("inf") or score_temp == float("-inf"):
        return score_temp
    else:
        score += score_temp

    # Check horizontal line
    score_temp = scoreOfLine(
                     gameState=gameState,
                     i=i,
                     j=j,
                     rowIncrement=0,
                     columnIncrement=-1,
                     firstRowCondition=-None,
                     secondRowCondition=None,
                     firstColumnCondition=-1,
                     secondColumnCondition=BOARD_SIZE_X,
                     player=player,
                     opponent=opponent
                 )
    if score_temp == float("inf") or score_temp == float("-inf"):
        return score_temp
    else:
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
    if score_temp == float("inf") or score_temp == float("-inf"):
        return score_temp
    else:
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
    if score_temp == float("inf") or score_temp == float("-inf"):
        return score_temp
    else:
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

    row = j + rowIncrement
    column = i + columnIncrement
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

    row = j - rowIncrement
    column = i - columnIncrement
    firstLoop = True
    while (
        row != secondRowCondition and
        column != secondColumnCondition and
        gameState[row][column] != 0
    ):
        if firstLoop:
            firstLoop = False
            if currentInLine != gameState[row][column]:
                currentInLine = gameState[row][column]
                if valsInARow == 3 and currentInLine == player:
                    score += 1
                    valsInARow = 0
                    break
                elif valsInARow >= 4 and currentInLine == player:
                    return float("inf")
                elif valsInARow == 3 and currentInLine == opponent:
                    score -= 1
                    valsInARow = 0
                    break
                elif valsInARow >= 4 and currentInLine == opponent:
                    return float("-inf")
            else:
                valsInARowPrev = valsInARow
                valsInARow = 0

        if currentInLine == gameState[row][column]:
            valsInARow += 1
        else:
            break
        row -= rowIncrement
        column -= columnIncrement

    if valsInARowPrev:
        if (valsInARow >= 4 or
            valsInARowPrev >= 4 and
            currentInLine == player
        ):
            return float("inf")
        elif (valsInARow >= 4 or
            valsInARowPrev >= 4 and
            currentInLine == opponent
        ):
            return float("-inf")

    else:
        if valsInARow >= 4 and currentInLine == player:
            return float("inf")
        elif valsInARow >= 4 and currentInLine == opponent:
            return float("-inf")

    if valsInARow + valsInARowPrev >= 3 and currentInLine == player:
        score += 1
    elif valsInARow + valsInARowPrev >= 3 and currentInLine == opponent:
        score -= 1

    return score
