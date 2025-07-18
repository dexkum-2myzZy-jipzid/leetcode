#!/usr/bin/env python3


class Solution:
    def strangePrinter(self, s: str) -> int:
        # min turn
        # convert s -> "aaabb" -> 'ab'

        t = []

        for i in range(len(s)):
            if t and s[i] == t[-1]:
                continue
            else:
                t.append(s[i])

        s = "".join(t)
        # print(s)

        n = len(s)
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                # merge segment
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k][j] - 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k][j])

        return dp[0][n - 1]
