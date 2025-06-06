#!/usr/bin/env python3


# multi dimensional dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[i][k][0/1] i: ith day, k transaction times, 0/1 hold stock or not
        # no stock
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # hold stock
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        n = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(k + 1):
            dp[0][i][1] = -prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        # print(dp)

        return dp[n - 1][k][0]
