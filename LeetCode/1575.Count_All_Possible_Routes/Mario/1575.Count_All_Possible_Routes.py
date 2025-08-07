#!/usr/bin/env python3

from typing import List


class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        # fule = abs(location[i] - location[j])
        # [2,3,6,8,4]
        #  0 1 2 3 4

        # dp[i][k] represents the count of routes when arrived at ith city with k fuel remaining
        # for next_city j in range(n):
        #   if k >= abs(location[i] - location[j]):
        #       dp[j][k-cost] += dp[i][k]

        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]

        # init dp
        dp[start][fuel] = 1

        for k in range(fuel, 0, -1):
            for i in range(n):
                if dp[i][k] == 0:
                    continue

                for j in range(n):
                    if i == j:
                        continue
                    cost = abs(locations[i] - locations[j])
                    if k >= cost:
                        dp[j][k - cost] = (dp[j][k - cost] + dp[i][k]) % MOD

        # for r in dp:
        #     print(r)

        return sum(dp[finish]) % MOD
