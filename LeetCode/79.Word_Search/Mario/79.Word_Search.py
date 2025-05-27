#!/usr/bin/env python3


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(start, i, j):
            if start == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[start]:
                return

            c = board[i][j]
            board[i][j] = "#"

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if backtrack(start + 1, i + di, j + dj):
                    board[i][j] = c
                    return True

            board[i][j] = c
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j):
                    return True

        return False
