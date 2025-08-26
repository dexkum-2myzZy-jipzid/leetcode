#!/usr/bin/env python3

from collections import defaultdict


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # knapsack problem
        cost_dic = defaultdict(str)
        for i, c in enumerate(cost):
            cost_dic[c] = str(i + 1)

        # print(cost_dic)
        costs = sorted(cost_dic.keys())
        n = len(costs)

        def compare(a, b):
            if len(a) != len(b):
                return len(a) > len(b)
            else:
                return a > b

        dp = [None] * (target + 1)
        dp[0] = ""

        # init dp
        for t in range(costs[0], target + 1):
            for c in costs:
                if t - c >= 0 and dp[t - c] is not None:
                    tmp = dp[t - c] + cost_dic[c]
                    if dp[t] is None or compare(tmp, dp[t]):
                        dp[t] = tmp

        return dp[target] if dp[target] else "0"
