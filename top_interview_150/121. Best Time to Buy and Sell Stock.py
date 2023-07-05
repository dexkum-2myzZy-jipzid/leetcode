#!/usr/bin/env python3

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price-min_price)
        return max_profit
