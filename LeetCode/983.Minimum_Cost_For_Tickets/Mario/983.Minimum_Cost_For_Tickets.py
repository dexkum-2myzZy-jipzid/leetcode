#!/usr/bin/env python3

"""
dp[i] min cost at ith day

min(dp[i-1], dp[i-7], dp[i-30]) (i-1 >=0 and i-7 >=0 and i-30 >= 0)
"""


from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        last_day = days[n - 1]
        dp = [0] * (last_day + 1)

        day_set = set(days)
        for i in range(1, last_day + 1):
            # ith has 3 options
            if i not in day_set:
                dp[i] = dp[i-1]
            else:
                cost_1 = dp[i - 1] + costs[0]
                cost_7 = dp[max(0, i - 7)] + costs[1]
                cost_30 = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(cost_1, cost_7, cost_30)


        # print(dp)

        return dp[last_day]
