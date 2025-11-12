#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf
from functools import cache


class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:

        # (0, 0) -> (m-1, n-1) only right or down
        #  cost <= k
        # [0, 1],
        # [2, 0]

        # (max_score, cost)

        # prev state -> current state
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            # out of boundary, return score 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return -inf

            score = grid[i][j]
            cost = 1 if score > 0 else 0

            if k - cost < 0:
                return -inf

            if i == m - 1 and j == n - 1:
                return score

            right = dfs(i, j + 1, k - cost) + score
            down = dfs(i + 1, j, k - cost) + score

            return max(right, down)

        res = dfs(0, 0, k)
        return -1 if res == -inf else res
