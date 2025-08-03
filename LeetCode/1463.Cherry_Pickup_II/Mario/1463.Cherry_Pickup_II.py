#!/usr/bin/env python3


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # dp[row][rob1][rob2] represents max num of cherries both robots will take from top to row grid
        # dp[i][j][k] from 3 directions
        # dp[i][j][k] = grid[i][j] + grid[i][k] + max(dp[i-1][j+dj][k+dk])
        # where dj, dk in [-1, 0, 1] (9 combinations total)
        # Note: if j == k, only count grid[i][j] once

        m, n = len(grid), len(grid[0])

        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]

        # init
        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        for i in range(1, m):
            for j in range(n):
                for k in range(n - 1, -1, -1):
                    cherries = grid[i][j] + grid[i][k]
                    if j == k:
                        cherries >>= 1

                    for dj in [-1, 0, 1]:
                        for dk in [-1, 0, 1]:
                            nj, nk = j + dj, k + dk

                            # fliter invalid case
                            if 0 <= nj < n and 0 <= nk < n and dp[i - 1][nj][nk] != -1:
                                dp[i][j][k] = max(
                                    dp[i][j][k], cherries + dp[i - 1][nj][nk]
                                )

        return max(
            dp[m - 1][i][j] for i in range(n) for j in range(n) if dp[m - 1][i][j] != -1
        )
