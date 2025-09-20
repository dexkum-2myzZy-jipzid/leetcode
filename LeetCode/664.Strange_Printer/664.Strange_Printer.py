#!/usr/bin/env python3


class Solution:
    def strangePrinter(self, s: str) -> int:
        tmp = []
        for i, c in enumerate(s):
            if tmp and tmp[-1] == c:
                continue
            else:
                tmp.append(c)
        s = "".join(tmp)

        n = len(s)
        dp = [[inf] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break

                if s[i] == s[j]:
                    dp[i][j] = dp[i][j] = min(dp[i][j], dp[i][j - 1])
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        # for r in dp:
        #     print(r)

        return dp[0][n - 1]
