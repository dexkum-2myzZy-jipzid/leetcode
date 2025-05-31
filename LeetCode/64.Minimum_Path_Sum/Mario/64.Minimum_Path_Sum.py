#!/usr/bin/env python3


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] means the min sum to get grid[i][j]
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        m, n = len(grid), len(grid[0])

        dp = [[math.inf] * n for _ in range(m)]

        # init dp, first row and first colums
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = cur
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + cur
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + cur
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + cur

        return dp[m - 1][n - 1]
