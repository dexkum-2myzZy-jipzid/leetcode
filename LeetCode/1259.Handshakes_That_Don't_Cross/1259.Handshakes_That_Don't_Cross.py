#!/usr/bin/env python3


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # numPeople is even
        # around circle
        # 2, 4, 6

        # dp[i] means the nun of way
        # dp[i] = dp[i-2](new one connected) + dp[i-2](last connect first)
        # dp[2] * dp[i-4] + dp[4] * dp[i-6] + ... + dp[i-2]

        MOD = 10**9 + 7

        dp = [0] * (numPeople + 1)

        # init dp
        dp[0] = 1
        dp[2] = 1

        for i in range(4, numPeople + 1, 2):
            for j in range(0, i - 2 + 1, 2):
                # print(f"i:{i}\tj:{j}")
                if i - 2 - j >= 0:
                    dp[i] = (dp[i] + dp[j] * dp[i - 2 - j]) % MOD
        # print(dp)

        return dp[numPeople]
