#!/usr/bin/env python3


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]

        # dp[i][j] max coins in (i, j), no include i and j

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        # [1, n-2]

        for l in range(2, n + 2):
            for i in range(0, n + 2):
                j = i + l
                if j >= n + 2:
                    break
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + points[i] * points[k] * points[j],
                    )

        return dp[0][n + 1]
