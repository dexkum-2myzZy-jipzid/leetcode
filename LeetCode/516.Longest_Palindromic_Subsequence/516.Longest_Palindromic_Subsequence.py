#!/usr/bin/env python3


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] means longest pali in s[i:j]

        # dp[i][j]:
        # s[i+1] == s[j-1], dp[i][j] + 2
        # s[i+1] != s[j-1]: max(dp[i+1][j], dp[i][j-1])

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            if i + 1 < n:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = 2
                else:
                    dp[i][i + 1] = 1

        # l: length
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # print(dp)

        return dp[0][n - 1]
