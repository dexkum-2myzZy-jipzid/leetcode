#!/usr/bin/env python3


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols, diag1, diag2 = set(), set(), set()

        def backtracking(row):
            nonlocal res
            if row == n:
                res += 1
                return

            for c in range(n):
                if c in cols or (row + c) in diag1 or (row - c) in diag2:
                    continue

                cols.add(c)
                diag1.add(row + c)
                diag2.add(row - c)

                backtracking(row + 1)

                cols.remove(c)
                diag1.remove(row + c)
                diag2.remove(row - c)

        backtracking(0)

        return res
