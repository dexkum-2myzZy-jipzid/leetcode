#!/usr/bin/env python3


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i][0] for ith stone, alice can get max score
        # dp[i][1] bob

        n = len(stoneValue)
        dp = [-inf for _ in range(n + 1)]
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(3):
                if i + j < n:
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])

        # for r in dp:
        #     print(r)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
