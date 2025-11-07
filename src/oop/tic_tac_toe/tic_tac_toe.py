from abc import ABC, abstractmethod


class TicTacToeBase(ABC):
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    @abstractmethod
    def make_move(self, row, col):
        pass

    @abstractmethod
    def check_who_won(self):
        pass

    @abstractmethod
    def game_is_over(self):
        pass


class TicTacToe(TicTacToeBase):
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_who_won(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Check for draw
        for row in self.board:
            if ' ' in row:
                return None
        return 'Draw'

    def game_is_over(self):
        if self.check_who_won():
            return True
        for row in self.board:
            if ' ' in row:
                return False
        return True
