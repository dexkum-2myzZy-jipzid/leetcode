#!/usr/bin/env python3


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s = t
        # dp[i][j] means the num of distinct subsequences of s[:i] which equals s[:j]

        m, n = len(s), len(t)
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 if s[0] == t[0] else 0
        # init first row & first col
        # s = "", t = "r"
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + (1 if s[i] == t[0] else 0)

        for j in range(1, n):
            for i in range(1, m):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m - 1][n - 1]
