#!/usr/bin/env python3
from math import inf


class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        # dp[i][j][k] represents minimum cost for first i houses, k neighborhoods, ith house with color j
        # Transition:
        # 1. Same color as previous: dp[i][j][k] = dp[i-1][j][k] + cost[i][j]
        # 2. Different color: dp[i][j][k] = min(dp[i-1][x][k-1]) + cost[i][j] for all x != j

        dp = [[[inf] * (target + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        # 0 houses, 0 color, 0 neigh
        dp[0][0][0] = 0

        for i in range(1, m + 1):
            house = houses[i - 1]
            for j in range(1, n + 1):
                # house was painted
                if house != 0 and house != j:
                    continue

                cur_cost = 0 if house > 0 and house == j else cost[i - 1][j - 1]
                for jj in range(n + 1):
                    for k in range(1, min(target, i) + 1):
                        # same color as previous
                        if jj == j:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][jj][k] + cur_cost)
                        else:  # diff color
                            dp[i][j][k] = min(
                                dp[i][j][k], dp[i - 1][jj][k - 1] + cur_cost
                            )

        res = inf
        for j in range(1, n + 1):
            res = min(res, dp[m][j][target])

        return res if res != inf else -1
