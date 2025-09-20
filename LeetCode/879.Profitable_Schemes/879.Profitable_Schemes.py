#!/usr/bin/env python3


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        # join 1 crime, not join another
        # the num of members <= n, profit >= minProfit
        # return the num of schemes

        # 1. the num of members n,
        # 2. sum profit
        # dp[i][j]

        MOD = 10**9 + 7
        m = minProfit
        crimes = sorted(list(zip(group, profit)))

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # init dp, 0 member, 0 profit
        dp[0][0] = 1

        # i members, j profit
        for g, p in crimes:
            for i in range(n, g - 1, -1):
                for j in range(m, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % MOD

        # for r in dp:
        #     print(r)

        return sum(dp[i][m] for i in range(n + 1)) % MOD
