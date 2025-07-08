#!/usr/bin/env python3


# LCS dp
class Solution:
    def minInsertions(self, s: str) -> int:
        # min step make s pali

        # s: leetcode leetcodocteel
        # t: edocteel

        # dp[i][j] s[:i] t[:j] mini step to make the same
        # s[i] == s[j]: dp[i][j] = dp[i-1][j-1]
        # not equal: dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

        n = len(s)
        t = s[::-1]

        dp = [[inf] * (n + 1) for _ in range(n + 1)]

        # init dp
        for i in range(n + 1):
            dp[0][i] = i
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # not insert
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # insert s, or insert t
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)

        # print(dp)

        return dp[n][n] // 2


# dp insert character
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # dp[i][j]: s[i..j] 变回文的最少插入次数
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):  # 区间长度
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]
