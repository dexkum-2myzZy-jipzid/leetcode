#!/usr/bin/env python3


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # largest subset of strs at most m 0 and n 1

        # knapsack problem
        # dp[i][j] means largest subset that are at most i 0 and j 1
        # dp[i][j] = max(dp[i-x][j-y] + 1) for x, y in strs

        # convert strs to 1 and 0 tuples
        zero_one = []
        for e in strs:
            z, o = 0, 0
            for c in e:
                if c == "0":
                    z += 1
                elif c == "1":
                    o += 1
            zero_one.append((z, o))

        # print(zero_one)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for x, y in zero_one:
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)

        # print(dp)

        return dp[m][n]
