#!/usr/bin/env python3


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 1. + "0" zero times
        # 2. + "1" one tims

        # dp[i]:
        # take 1,  dp[i-zero]
        # take 2,  dp[i-one]
        # dp[i] = (dp[i-zero] + dp[i-one])

        # sum(dp[low:high])

        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            # append '0'
            if i >= zero:
                dp[i] += dp[i - zero]
                dp[i] %= MOD
            if i >= one:
                dp[i] += dp[i - one]
                dp[i] %= MOD

        res = 0
        for i in range(low, high + 1):
            res += dp[i]
            res %= MOD

        return res
