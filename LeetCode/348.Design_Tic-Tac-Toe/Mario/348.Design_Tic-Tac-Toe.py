#!/usr/bin/env python3


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        # player 1 add 1, player 2 add -1
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        # diagonal
        if row == col:
            self.diag += val

        # anti_diagonal
        if row + col == self.n - 1:
            self.anti_diag += val

        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diag) == self.n
            or abs(self.anti_diag) == self.n
        ):
            return player

        return 0
