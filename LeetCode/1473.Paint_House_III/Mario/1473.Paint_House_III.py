#!/usr/bin/env python3
from math import inf


class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        # a row of m houses
        # neighborhoods
        # house: i color, 0 no painted
        # cost: i house, j+1 color
        # min cost: all remaining houses target neigh, if not -1

        # state: cost: ith house with j color, k group
        # dp[i][j][k] = score
        # if ith house, has j color, dp[i][j-1][k] = 0
        # if ith house: no painted, dp[i][x] x in [0, n]

        dp = [[[inf] * target for _ in range(n)] for _ in range(m)]

        # init dp
        if houses[0] != 0:
            dp[0][houses[0] - 1][0] = 0
        else:
            for i, c in enumerate(cost[0]):
                dp[0][i][0] = c

        # print(dp)
        for i in range(1, m):
            color = houses[i]
            for j in range(n):
                if color != 0 and color - 1 != j:
                    continue
                for k in range(target):
                    # same color as previous house
                    if dp[i - 1][j][k] != inf:
                        val = dp[i - 1][j][k]
                        if color == 0:
                            val += cost[i][j]
                        dp[i][j][k] = min(dp[i][j][k], val)
                    # different color, new neighborhood
                    if k > 0:
                        for jj in range(n):
                            if jj == j:
                                continue
                            if dp[i - 1][jj][k - 1] != inf:
                                val = dp[i - 1][jj][k - 1]
                                if color == 0:
                                    val += cost[i][j]
                                dp[i][j][k] = min(dp[i][j][k], val)

        res = inf
        for j in range(n):
            if dp[m - 1][j][target - 1] < res:
                res = dp[m - 1][j][target - 1]

        return -1 if res == inf else res
