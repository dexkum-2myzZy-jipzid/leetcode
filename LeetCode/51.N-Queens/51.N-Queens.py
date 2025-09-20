#!/usr/bin/env python3

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        matrix = [["." for _ in range(n)] for _ in range(n)]

        cols, diag1, diag2 = set(), set(), set()

        def backtracking(row):
            if row == n:
                solution = ["".join(r) for r in matrix]
                res.append(solution)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                matrix[row][col] = "Q"

                backtracking(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                matrix[row][col] = "."

        backtracking(0)

        return res