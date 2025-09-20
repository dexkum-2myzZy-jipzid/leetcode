#!/usr/bin/env python3


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # state: held / sell stock
        # held[i] = max(held[i-1], sold[i]-prices[i])
        # sold[i] = max(sold[i-1], held[i-1] + prices[i] - fee)

        n = len(prices)

        held = [0] * n
        sold = [0] * n

        # init
        held[0], sold[0] = -prices[0], 0

        for i in range(1, n):
            held[i] = max(held[i - 1], sold[i - 1] - prices[i])
            sold[i] = max(sold[i - 1], held[i - 1] + prices[i] - fee)

        # print(f"held:{held}\nsold:{sold}")

        return sold[n - 1]
