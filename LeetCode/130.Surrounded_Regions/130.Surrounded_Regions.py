#!/usr/bin/env python3


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # traverse all the edges of board
        # if hit '0', dfs it and makr it related,
        # then traverse all cell, then turn '0' which not connecnted to edge turn '1'

        m, n = len(board), len(board[0])

        rows, cols = [0], [0]
        if m - 1 != 0:
            rows.append(m - 1)
        if n - 1 != 0:
            cols.append(n - 1)

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                return

            board[i][j] = "#"

            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        # four edges
        for i in rows:
            for j in range(n):
                if board[i][j] == "O":
                    dfs(i, j)

        for i in range(m):
            for j in cols:
                if board[i][j] == "O":
                    dfs(i, j)

        # traverse all cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
