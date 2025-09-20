#!/usr/bin/env python3


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # the num of ways you can earn exactly target points

        MOD = 10**9 + 7

        n = len(types)

        # ith target, ith type
        # dp[target][ith]

        dp = [0] * (target + 1)

        # target = 0, ways = 1
        dp[0] = 1

        # enumerate types
        for i in range(1, n + 1):
            count, mark = types[i - 1]
            # 0-1 knapsack
            for j in range(target, mark - 1, -1):
                for k in range(1, count + 1):
                    pts = k * mark
                    if j - pts >= 0:
                        dp[j] = (dp[j] + dp[j - pts]) % MOD
                    else:
                        break

        # print(dp)

        return dp[target]
