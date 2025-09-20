#!/usr/bin/env python3


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0.0] * (target + 1) for i in range(n + 1)]
        dp[0][0] = 1.0

        for i in range(1, n + 1):
            p = prob[i - 1]
            for j in range(target + 1):
                # face head
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * p
                # not face head
                dp[i][j] += dp[i - 1][j] * (1 - p)

        return dp[n][target]
