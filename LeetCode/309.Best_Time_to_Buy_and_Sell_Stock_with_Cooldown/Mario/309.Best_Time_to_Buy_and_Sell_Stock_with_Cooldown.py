#!/usr/bin/env python3


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit / as many transations as you like
        # state: hold -> sell -> cooldown -> hold

        # held[i] = max(held[i-1], reset[i-1] - prices[i]) # hold stock before ith day / hold ith stock
        # sold[i] = held[i-1] + prices[i] # sell ith prices to get profit
        # reset[i] = max(sold[i-1], reset[i-1]) # start to cooldown / keep cooldown

        n = len(prices)

        held = -prices[0]
        sold = 0
        reset = 0

        for i in range(1, n):
            next_held = max(held, reset - prices[i])
            next_sold = prices[i] + held
            next_reset = max(reset, sold)

            held, sold, reset = next_held, next_sold, next_reset

        return max(sold, reset)
