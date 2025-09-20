#!/usr/bin/env python3


class Solution:
    def numTrees(self, n: int) -> int:
        # the num of combination of (A, B)
        # e.g 3
        # (dp[0] * dp[2]) + (dp[2] * dp[0]) + (dp[1] * dp[1])

        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
                print(f"i:{i}\tj:{j}\t(i-j-1):{i - j - 1}\tdp:{dp}")

        return dp[n]
