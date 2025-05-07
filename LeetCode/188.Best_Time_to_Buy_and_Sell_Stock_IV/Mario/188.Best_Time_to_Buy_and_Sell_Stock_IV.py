#!/usr/bin/env python3


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        k = 2
        today = prices[i]
        hold1 = max(pre_hold1, -today)
        sell1 = max(pre_sell1, today + hold1)

        hold2 = max(pre_hold2, sell1-today)
        sell2 = max(pre_sell2, today + hold2)

        => k
        dp = [-math.inf, 0] * k

        # hold
        dp[i+1][0] = max(dp[i][0], -today)
        # sell
        dp[i+1][1] = max(dp[i][1], today + dp[i+1][0])

        """

        n = len(prices)
        if n < 2:
            return 0

        dp = [[-math.inf, 0] for _ in range(k)]

        for p in prices:
            for i in range(k - 1, -1, -1):
                dp[i][1] = max(dp[i][1], p + dp[i][0])
                if i >= 1:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] - p)
                else:
                    dp[i][0] = max(dp[i][0], -p)

        return dp[k - 1][1]
