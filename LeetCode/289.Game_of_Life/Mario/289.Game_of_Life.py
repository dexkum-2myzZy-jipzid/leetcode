#!/usr/bin/env python3


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        < 2 dies, under
        2 or 3 lives, next
        > 3 dies, over
        dead cell = 3 live, re 
        """
        m, n = len(board), len(board[0])
        directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]

        for i in range(m):
            for j in range(n):
                nei = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] in [1, 2]:  # [live, was live]
                            nei += 1

                if board[i][j] == 1:
                    if nei < 2 or nei > 3:
                        board[i][j] = 2  # live -> dead, mark 2
                elif board[i][j] == 0:
                    if nei == 3:
                        board[i][j] = 3  # dead -> live mark 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
