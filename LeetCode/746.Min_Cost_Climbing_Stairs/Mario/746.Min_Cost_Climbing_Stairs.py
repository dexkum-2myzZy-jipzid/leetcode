#!/usr/bin/env python3


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        f0 = f1 = 0

        for i in range(2, n + 1):
            new_f1 = min(f1 + cost[i - 1], f0 + cost[i - 2])
            f1, f0 = new_f1, f1

        return f1
