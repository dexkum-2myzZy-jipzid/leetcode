#!/usr/bin/env python3


# dfs
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # abcdeca -> acdca k = 2
        # abbababa -> abababa k=1

        # dfs(l, r, k) dfs(0, len(s)-1, k)

        @cache
        def dfs(i, j, k):
            if k < 0:
                return False
            elif i >= j:  # k >= 0
                return True

            # k > 0
            if s[i] == s[j]:
                if dfs(i + 1, j - 1, k):
                    return True
            if dfs(i + 1, j, k - 1) or dfs(i, j - 1, k - 1):
                return True
            return False

        return dfs(0, len(s) - 1, k)


# dp
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        # dp[i][j] 表示 s[i:j+1] 最少要删几个变成回文
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):  # length 是区间长度
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1] <= k
