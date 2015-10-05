BOARD_SIZE_X = 7
BOARD_SIZE_Y = 6
SEARCH_DEPTH = 4

COMPUTER_PLAYER = 1
HUMAN_PLAYER = -1

def minimax(gameState, depth, player, opponent):
    availableMoves = BOARD_SIZE_X
    for i in range(0, BOARD_SIZE_X):
        if (gameState[0][i] != 0):
            availableMoves -= 1

    if (depth == 0 or availableMoves == 0):
        score = evaluateScore(gameState, COMPUTER_PLAYER, HUMAN_PLAYER)
        return None, score

    bestScore = None
    bestMove = None

    for i in range(0, BOARD_SIZE_X):
        if gameState[0][i] != 0:
            continue

        currentMove = [0, i]

        for j in range(1, BOARD_SIZE_Y):
            if (gameState[j][i] != 0):
                gameState[j-1][i] = player
                moveLocation[0] = j - 1
                break

        move, score = minimax(gameState, depth - 1, opponent, player)

        gameState[currentMove[0]][currentMove[1]] = 0

        if (player == COMPUTER_PLAYER):
            if (bestScore == None or score > bestScore):
                bestScore = score
                bestMove = currentMove
        else:
            if (bestScore == None or score < bestScore):
                bestScore = score
                bestMove = currentMove

    return bestMove, bestScore

def evaluateScore(gameState, player, opponent):
    score = 0
    currentInLine = 0
    valsInARow = 0

    for i in range(0, BOARD_SIZE_X):
        for j in range(0, BOARD_SIZE_Y):
            if (gameState[j][i] == 0):

                # Check vertical up
                row = j - 1
                column = i
                firstLoop = True
                while (row != -1 and gameState[row][column] != 0):
                    if (firstLoop):
                        currentInLine = gameState[row][column]
                        firstLoop = false
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row -= 1

                # Check vertical down
                row = j + 1
                firstLoop = True
                while (row != BOARD_SIZE_Y and gameState[row][column] != 0):
                    if (firstLoop):
                        firstLoop = false
                        if (currentInLine != gameState[row][column]):
                            currentInLine = gameState[row][column]
                            if (valsInARow >= 4 and currentInLine == player):
                                score += 1
                            elif (valsInARow >= 4 and currentInLine == opponent):
                                score -= 1
                            valsInARow = 0

                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row += 1

                if (valsInARow >= 4 and currentInLine == player):
                    score += 1
                elif (valsInARow >= 4 and currentInLine == opponent):
                    score -= 1
                valsInARow = 0

                # Check horizontal left
                row = j
                column = i - 1
                firstLoop = True
                while (column != -1 and gameState[row][column] != 0):
                    if (firstLoop):
                        currentInLine = gameState[row][column]
                        firstLoop = false
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    column -= 1

                # Check horizontal right
                column = i + 1
                firstLoop = True
                while (column != BOARD_SIZE_X and gameState[row][column] != 0):
                    if (firstLoop):
                        firstLoop = false
                        if (currentInLine != gameState[row][column]):
                            currentInLine = gameState[row][column]
                            if (valsInARow >= 4 and currentInLine == player):
                                score += 1
                            elif (valsInARow >= 4 and currentInLine == opponent):
                                score -= 1
                            valsInARow = 0
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    column += 1

                if (valsInARow >= 4 and currentInLine == player):
                    score += 1
                elif (valsInARow >= 4 and currentInLine == opponent):
                    score -= 1
                valsInARow = 0

                # Check diagonal 1 / - up and right
                row = j - 1
                column = i + 1
                firstLoop = True
                while (
                    row != -1 and
                    column != BOARD_SIZE_X and
                    gameState[row][column] != 0
                ):
                    if (firstLoop):
                        currentInLine = gameState[row][column]
                        firstLoop = false
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row -= 1
                    column += 1

                # Check diagonal 1 / - down and left
                row = j + 1
                column = i - 1
                firstLoop = True
                while (
                    row != BOARD_SIZE_Y and
                    column != -1 and
                    gameState[row][column] != 0
                ):
                    if (firstLoop):
                        firstLoop = false
                        if (currentInLine != gameState[row][column]):
                            currentInLine = gameState[row][column]
                            if (valsInARow >= 4 and currentInLine == player):
                                score += 1
                            elif (valsInARow >= 4 and currentInLine == opponent):
                                score -= 1
                            valsInARow = 0
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row += 1
                    column -= 1

                if (valsInARow >= 4 and currentInLine == player):
                    score += 1
                elif (valsInARow >= 4 and currentInLine == opponent):
                    score -= 1
                valsInARow = 0

                # Check diagonal 2 \ - up and left
                row = j - 1
                column = i - 1
                firstLoop = True
                while (
                    row != -1 and
                    column != -1 and
                    gameState[row][column] != 0
                ):
                    if (firstLoop):
                        currentInLine = gameState[row][column]
                        firstLoop = false
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row -= 1
                    column -= 1

                # Check diagonal 2 \ - down and right
                row = j + 1
                column = i + 1
                firstLoop = True
                while (
                    row != BOARD_SIZE_Y and
                    column != BOARD_SIZE_X and
                    gameState[row][column] != 0
                ):
                    if (firstLoop):
                        firstLoop = false
                        if (currentInLine != gameState[row][column]):
                            currentInLine = gameState[row][column]
                            if (valsInARow >= 4 and currentInLine == player):
                                score += 1
                            elif (valsInARow >= 4 and currentInLine == opponent):
                                score -= 1
                            valsInARow = 0
                    if (currentInLine == gameState[row][column]):
                        valsInARow += 1
                    else:
                        break
                    row += 1
                    column += 1

                if (valsInARow >= 4 and currentInLine == player):
                    score += 1
                elif (valsInARow >= 4 and currentInLine == opponent):
                    score -= 1
                valsInARow = 0


    return score

def bestMove(gameState, player, opponent):
    move, score = minimax(gameState, SEARCH_DEPTH, player, opponent)
    return move
