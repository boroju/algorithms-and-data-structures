import unittest
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_check_winner(self):
        game = TicTacToe()

        # Horizontal win
        game.board = [
            ['X', 'X', 'X'],
            ['O', ' ', 'O'],
            ['X', 'O', ' ']
        ]
        self.assertEqual(game.check_who_won(), 'X')

        # Diagonal win
        game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', ' ', ' ']
        ]
        self.assertEqual(game.check_who_won(), 'X')

        # Draw
        game.board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertEqual(game.check_who_won(), 'Draw')

    def test_game_is_over(self):
        game = TicTacToe()

        # Game over with a win
        game.board = [
            ['X', 'X', 'X'],
            ['O', ' ', 'O'],
            ['X', 'O', ' ']
        ]
        self.assertTrue(game.game_is_over())

        # Game over with a draw
        game.board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(game.game_is_over())

        # Game not over
        game.board = [
            ['X', ' ', 'X'],
            ['X', 'X', ' '],
            ['O', ' ', 'O']
        ]
        self.assertFalse(game.game_is_over())


if __name__ == '__main__':
    unittest.main()
