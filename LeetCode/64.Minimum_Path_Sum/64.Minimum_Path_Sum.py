#!/usr/bin/env python3


from math import inf


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # using dp
        # dp[i][j] represents the min sum from (0,0) to (i,j)
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                top = dp[i - 1][j] if i > 0 else inf
                left = dp[i][j - 1] if j > 0 else inf

                dp[i][j] = int(min(top, left)) + grid[i][j]

        return dp[m - 1][n - 1]
