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
        score = evaluateScore(gameState, COMPUTER_PLAYER)
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

def bestMove(gameState, player, opponent):
    move, score = minimax(gameState, SEARCH_DEPTH, player, opponent)
    return move

def evaluateScore(gameState, player):
    return float("inf")
