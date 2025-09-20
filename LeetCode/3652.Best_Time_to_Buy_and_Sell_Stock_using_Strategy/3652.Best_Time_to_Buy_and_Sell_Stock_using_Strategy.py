#!/usr/bin/env python3


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix = [0] * (n + 1)
        prefix_prices = [0] * (n + 1)

        for i in range(n):
            p, s = prices[i], strategy[i]
            prefix[i + 1] = prefix[i] + p * s
            prefix_prices[i + 1] = prefix_prices[i] + p

        res = prefix[-1]

        for i in range(n):
            j = i + k
            if j > n:
                break

            pre = prefix[j] - prefix[i]
            pre_p = prefix_prices[j] - prefix_prices[j - k // 2]
            # print(f"prefix sum:{pre}\tprefix prices:{pre_p}")
            res = max(res, prefix[-1] - pre + pre_p)

        return res
