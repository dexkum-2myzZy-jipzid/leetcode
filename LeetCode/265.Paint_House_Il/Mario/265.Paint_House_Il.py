#!/usr/bin/env python3


# O(m * n * n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # a row of n houses, k colors, cost is diff
        # no two adjacent houses have the same color.

        m, n = len(costs), len(costs[0])
        dp = [[0] * n for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(n):
                cost = costs[i - 1][j]
                # get pre dp[i-1]
                pre = min(dp[i - 1][k] for k in range(n) if k != j)
                dp[i][j] = cost + pre

        return min(dp[m])


# O(m * n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # a row of n houses, k colors, cost is diff
        # no two adjacent houses have the same color.

        m, n = len(costs), len(costs[0])

        pre_min0, pre_min1 = (0, -1), (0, -1)

        for i in range(m):
            cur_min0, cur_min1 = (inf, -1), (inf, -1)
            for j in range(n):
                cost = costs[i][j]
                cur_cost = 0
                if pre_min0[1] != j:
                    cur_cost = cost + pre_min0[0]
                else:
                    cur_cost = cost + pre_min1[0]

                if cur_cost <= cur_min0[0]:
                    cur_min1, cur_min0 = cur_min0, (cur_cost, j)
                elif cur_cost < cur_min1[0]:
                    cur_min1 = (cur_cost, j)

            pre_min0, pre_min1 = cur_min0, cur_min1

        return pre_min0[0]
