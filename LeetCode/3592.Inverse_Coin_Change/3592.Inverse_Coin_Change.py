#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        # 1 - indexed array
        # numWays = [1,2,3,4,15]
        # max amount = len(numWays)
        # dp[j] represent the num of ways to get amount j
        # init dp[0] = 1
        # iterate i from range(1, n+1)
        # diff = numWays[i-1] - dp[i]
        # if diff == 0: this set denominations is enough
        # if diff == 1: this set can add i, update dp from [i, n]
        # else: []

        n = len(numWays)

        dp = [0] * (n + 1)
        dp[0] = 1

        res = []

        for i in range(1, n + 1):
            diff = numWays[i - 1] - dp[i]
            if diff == 0:
                continue
            elif diff == 1:
                res.append(i)
                for j in range(i, n + 1):
                    dp[j] += dp[j - i]
            else:
                return []

        return res
