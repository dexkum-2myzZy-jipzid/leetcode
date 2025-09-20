#!/usr/bin/env python3


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] the count to reach this (i, j) point
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # init
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        # 0th row
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
        # 0th column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # print(dp)
        return dp[m - 1][n - 1]
