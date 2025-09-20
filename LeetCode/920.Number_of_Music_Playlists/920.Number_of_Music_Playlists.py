#!/usr/bin/env python3


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # n diff songs, goal songs
        # 1. played once
        # 2. played again, if k other songs played

        # dp[i][j] means i length playlist with j unique songs
        # add unique songs
        # dp[i][j] = dp[i-1][j-1] * (n-j+1)
        # add same songs
        # dp[i][j] = dp[i-1][j] +  max(j - k, 0)

        MOD = 10**9 + 7

        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        # init dp
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # add unique songs
                dp[i][j] = (dp[i - 1][j - 1] * (n - j + 1)) % MOD
                # add songs we played before
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]
