#!/usr/bin/env python3


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # a row of n houses, red, blue or green, cost is diff
        # 0: red, 1:blue, 2:green
        # no two adjacent houses have the same color.

        # dp[i] = min(
        #    min(dp[i-1][1:2]) + costs[i][0],
        #     min(dp[i-1][0],dp[i-1][2]) + costs[i][1],
        # .  min(dp[i-1][0],dp[i-1][1]) + costs[i][2],)

        n = len(costs)
        dp = [[0] * 3 for _ in range(n + 1)]

        for i in range(1, n + 1):
            red, blue, green = costs[i - 1]
            dp[i][0] = red + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = blue + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = green + min(dp[i - 1][0], dp[i - 1][1])

        return min(dp[n])
