#!/usr/bin/env python3

from math import inf
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # stick n units
        # cost = len(cur length of stick)
        # total_cost = sum(cost)
        # return minimum total cost

        # n = min(n-1, 100) + 1
        # dp[i][j] represents total cost of cuts[i:j]
        # for k in (i, j), dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]) + (cuts[j] - cuts[i]))

        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[inf] * m for _ in range(m)]

        # init dp
        for i in range(m - 1):
            dp[i][i + 1] = 0

        for length in range(3, m + 1):
            for i in range(m):
                j = i + length - 1
                if j >= m:
                    break
                for k in range(i + 1, j):
                    # [0, 1, 3] dp[0][1] dp[1][3]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        # for r in dp:
        #     print(r)

        return dp[0][m - 1]
