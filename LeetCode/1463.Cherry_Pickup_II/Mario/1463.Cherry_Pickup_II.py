#!/usr/bin/env python3


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[row][col1][col2]
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]

        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        for i in range(1, m):  # row
            for j in range(n):  # robot1 col
                for k in range(n - 1, -1, -1):  # robot2 col
                    cherries = grid[i][j]
                    if j != k:
                        cherries += grid[i][k]

                    max_pre = -1
                    for dj in [-1, 0, 1]:
                        for dk in [-1, 0, 1]:
                            pj, pk = j + dj, k + dk

                            # filter invalid case
                            if 0 <= pj < n and 0 <= pk < n and dp[i - 1][pj][pk] != -1:
                                max_pre = max(max_pre, dp[i - 1][pj][pk])

                    if max_pre != -1:
                        dp[i][j][k] = cherries + max_pre

        result = 0
        for col1 in range(n):
            for col2 in range(n):
                if dp[m - 1][col1][col2] != -1:
                    result = max(result, dp[m - 1][col1][col2])

        # for row in dp:
        #     print(row)

        return result
