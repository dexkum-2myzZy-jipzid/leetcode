#!/usr/bin/env python3


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # take beginning or end
        # A first, B next

        # dp[i][j]: max diff score alica can get over bob in the pilses range [i, j]
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        # init
        for i, p in enumerate(piles):
            dp[i][i] = p

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                else:
                    dp[i][j] = max(
                        piles[i] - dp[i + 1][j],  # take left
                        piles[j] - dp[i][j - 1],  # take right
                    )

        return dp[0][n - 1] > 0


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
