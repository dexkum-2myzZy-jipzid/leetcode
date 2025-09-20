#!/usr/bin/env python3


# dp
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # m*n grid
        # Return the number of strictly increasing paths

        # dp[i][j].  dp[i][j] = sum(dp[i-1][j], dp[i][j-1])

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[1] * n for _ in range(m)]

        DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cell = []

        for i in range(m):
            for j in range(n):
                cell.append((grid[i][j], i, j))
        cell.sort()

        for val, i, j in cell:
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % MOD

        res = 0
        for i in range(m):
            for j in range(n):
                res = (res + dp[i][j]) % MOD

        return res


# dfs
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # m*n grid
        # Return the number of strictly increasing paths

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cell = []

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            res = 1
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    res = (res + dfs(ni, nj)) % MOD
            dp[i][j] = res
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                res = (res + dfs(i, j)) % MOD

        return res
