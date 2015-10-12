import unittest
import connect4

class TestHeuristic(unittest.TestCase):

    def setUp(self):
        self.player = connect4.COMPUTER_PLAYER
        self.opponent = connect4.HUMAN_PLAYER

    def test_score_potential_wins(self):
        gameState = [
            [ 1, 0,  0,  0, 0, 0, 0],
            [-1, 0,  0,  0, 0, 0, 0],
            [-1, 0,  1, -1, 0, 0, 0],
            [-1, 0, -1,  1, 0, 0, 0],
            [ 1, 0,  1,  1, 0, 0, 0],
            [-1, 0, -1, -1, 0, 0, 0]
        ]
        score = connect4.evaluateScore(gameState, self.player, self.opponent)
        self.assertEqual(score, 0)

        gameState = [
            [ 1, 0,  0,  0,  0, 0, 0],
            [-1, 0,  0,  0,  0, 0, 0],
            [ 1, 0,  1,  1,  1, 0, 0],
            [-1, 0, -1, -1,  1, 0, 1],
            [-1, 0, -1, -1,  1, 0, 1],
            [-1, 0, -1, -1, -1, 0, 1]
        ]
        score = connect4.evaluateScore(gameState, self.player, self.opponent)
        self.assertEqual(score, 0)

    def test_score_computer_win(self):
        gameState = [
            [-1,  0,  0,  0, 0, 0, 0],
            [-1,  0,  0,  0, 0, 0, 0],
            [ 1,  0,  0,  0, 0, 0, 0],
            [-1,  1,  0,  0, 0, 0, 0],
            [ 1,  1,  1,  0, 0, 0, 0],
            [-1, -1, -1,  1, 0, 0, 0]
        ]
        score = connect4.evaluateScore(gameState, self.player, self.opponent)
        self.assertEqual(score, float("inf"))

    def test_score_opponent_win(self):
        gameState = [
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 1],
            [-1, 0, 0, 0, 0, 0, 1],
            [-1, 0, 0, 0, 0, 0, 1]
        ]
        score = connect4.evaluateScore(gameState, self.player, self.opponent)
        self.assertEqual(score, float("-inf"))

        gameState = [
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 1],
            [ 0, 0, 0, 0, 0, 0, 1],
            [-1,-1,-1,-1, 0, 0, 1]
        ]
        score = connect4.evaluateScore(gameState, self.player, self.opponent)
        self.assertEqual(score, float("-inf"))


class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.player = connect4.COMPUTER_PLAYER
        self.opponent = connect4.HUMAN_PLAYER

    def test_prevent_defeat(self):

        gameState = [
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0,-1],
            [ 1, 0, 0, 0, 0, 0,-1],
            [ 1, 0, 0, 0, 0, 0,-1]
        ]
        move = connect4.bestMove(gameState, self.player, self.opponent)
        self.assertEqual(move, 6)


if __name__ == "__main__":
    unittest.main()
