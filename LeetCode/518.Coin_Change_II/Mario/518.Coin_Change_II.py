#!/usr/bin/env python3


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[amount] means the num of combination
        # dp[i] = sum(dp[i-c]) for c in coins

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
                # print(dp)

        return dp[amount]
