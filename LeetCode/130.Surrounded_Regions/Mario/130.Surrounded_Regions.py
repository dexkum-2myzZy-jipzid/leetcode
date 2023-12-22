#!/usr/bin/env python3

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def solveHelper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] == "O":
                board[i][j] = "A"
                for a, b in directions:
                    solveHelper(i+a, j+b)

        # check 4 sides, find "O"
        for i in range(n):
            if board[0][i] == "O":
                solveHelper(0, i)

        if m > 1:
            for i in range(n):
                if board[m-1][i] == "O":
                    solveHelper(m-1, i)

        for i in range(m):
            if board[i][0] == "O":
                solveHelper(i, 0)

        if n > 1:
            for i in range(m):
                if board[i][n-1] == "O":
                    solveHelper(i, n-1)

        # flip "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"
