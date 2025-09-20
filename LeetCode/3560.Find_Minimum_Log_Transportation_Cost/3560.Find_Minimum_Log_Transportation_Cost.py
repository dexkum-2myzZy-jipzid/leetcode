#!/usr/bin/env python3


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # at most k unit

        cost = 0
        if k < n:
            cost += (n - k) * k
        if k < m:
            cost += (m - k) * k

        return cost
