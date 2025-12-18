#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # using dp
        # dp[i][j] represent the nun of ways from (0, 0) to (i, j)
        # # from top or from left
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        dp = [[0] * n for _ in range(m)]

        # init dp
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                top = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] += top + left

        return dp[m - 1][n - 1]
