#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:

        # dfs(i, j, move)
        # 1. move > maxMove: return 0
        # 2. i, j out of boundary: return 1
        # 3. i and j in boundary: continue try dfs 4 directions, dfs(ni, nj, move+1)

        MOD = 10**9 + 7
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        @cache
        def dfs(i: int, j: int, move: int) -> int:
            if move > maxMove:
                return 0

            if not (0 <= i < m and 0 <= j < n):
                return 1

            res = 0
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                res = (res + dfs(ni, nj, move + 1)) % MOD

            return res

        return dfs(startRow, startColumn, 0)
