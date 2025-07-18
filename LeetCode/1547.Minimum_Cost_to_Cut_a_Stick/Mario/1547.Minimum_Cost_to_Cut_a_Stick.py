#!/usr/bin/env python3


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()

        m = len(cuts)
        dp = [[inf] * m for _ in range(m)]

        for i in range(m - 1):
            dp[i][i + 1] = 0

        for i in range(2, m):
            for l in range(m):
                r = l + i
                if r >= m:
                    break
                for k in range(l + 1, r):
                    dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + cuts[r] - cuts[l])

        return dp[0][m - 1]
