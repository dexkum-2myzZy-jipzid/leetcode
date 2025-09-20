#!/usr/bin/env python3


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5]
        if n <= 3:
            return dp[n - 1]

        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        prefix[0], prefix[1], prefix[2] = 1, 2, 4

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * prefix[i - 3]) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        return dp[n]


# new dp way
class Solution:
    def numTilings(self, n: int) -> int:
        """
        ith.    pre
        1.      4
        1 0     o
        1 0     o

        2.      3      1
        1 1     x x    x x
        1 0     o      x

        3.     1       2
        1 0.   x       o
        1 1.   x x.    x x

        4.     4.      2      3     1
        1 1.   o x.    o x.   x x.  x x
        1 1.   o x.    x.x.   x o.  x x
        """
        MOD = 10**9 + 7
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (
                ((dp[i - 1][0] + dp[i - 1][1]) % MOD + dp[i - 1][2]) % MOD
                + dp[i - 1][3]
            ) % MOD
        return dp[n][3]
