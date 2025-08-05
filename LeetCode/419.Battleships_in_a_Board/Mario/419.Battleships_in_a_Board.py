#!/usr/bin/env python3


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # m * n
        m, n = len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    # check (i-1, j) or (i, j-1) cell
                    # check left first
                    left, top = True, True
                    if 0 <= i - 1 and board[i - 1][j] == "X":
                        top = False
                    if 0 <= j - 1 and board[i][j - 1] == "X":
                        left = False
                    if left and top:
                        res += 1

        return res
