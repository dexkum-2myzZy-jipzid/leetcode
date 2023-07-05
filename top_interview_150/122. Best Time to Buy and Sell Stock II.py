#!/usr/bin/env python3

# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = prices[0]
        res = 0
        for i in range(1, len(prices)):
            current = prices[i]
            if current > pre:
                res += current-pre
            pre = current
        return res
