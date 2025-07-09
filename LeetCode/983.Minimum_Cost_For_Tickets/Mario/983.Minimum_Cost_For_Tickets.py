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
                dp[i] = dp[i - 1]
            else:
                cost_1 = dp[i - 1] + costs[0]
                cost_7 = dp[max(0, i - 7)] + costs[1]
                cost_30 = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(cost_1, cost_7, cost_30)

        # print(dp)

        return dp[last_day]


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i]

        # dp[i][0]: buy 1 day pass
        # dp[i][1]: buy 7 day pass
        # dp[i][2]: buy 30 day pass

        # reverse dp
        # dp[i][0] = cost[0] + min(dp[i+1])
        # dp[i][1] = find(days[i] + 6) + min(dp[x])
        # dp[i][2] = find(days[i] + 29) + min(dp[x])

        n = len(days)
        dp = [[0] * 3 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            # buy 1-day pass
            dp[i][0] = costs[0] + min(dp[i + 1])

            # buy 7-day pass
            nxt = days[i] + 6
            j = bisect.bisect_right(days, nxt)
            dp[i][1] = costs[1] + min(dp[j])

            # buy 30-day pass
            nxt30 = days[i] + 29
            k = bisect.bisect_right(days, nxt30)
            dp[i][2] = costs[2] + min(dp[k])

        # print(dp)

        return min(dp[0])
