#!/usr/bin/env python3


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ?: single char
        # *: any (include " ")
        # s, p lowercase

        n, m = len(s), len(p)

        # dp[i][j] = s[:i] can math with p[:j]
        #  1. s[i] == p[j] or p[j] in "*?" dp[i][j] = dp[i-1][j-1]
        #  2. p[j] == "*"  dp[i][j] = dp[i][j-1] or dp[i-1][j]
        #  3. s[i] != p[j]  dp[i][j] = False

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # init dp
        # s "", p ""
        dp[0][0] = True
        # s = "", p = "...."
        for i in range(1, m + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cs, cp = s[i - 1], p[j - 1]
                if cs == cp or cp == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif cp == "*":
                    # cp = "" / cp can match cs
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[n][m]
