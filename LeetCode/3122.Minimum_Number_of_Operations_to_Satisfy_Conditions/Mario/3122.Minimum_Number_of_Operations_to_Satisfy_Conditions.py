#!/usr/bin/env python3


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # op: any cell -> no-neg num
        m, n = len(grid), len(grid[0])

        # key: how to handle neighbor cols val
        # min ->  n * m - max unchange val

        # dp[i][j]  if ith col all num change to num j,
        # so min ops need to change from [0 - ith] cols

        dp = [[0] * 10 for _ in range(n)]

        for j in range(n):
            # count val
            for i in range(m):
                val = grid[i][j]
                dp[j][val] += 1

            for k in range(10):
                dp[j][k] = m - dp[j][k]
                # if col is not 0th, so need to add pre col
                if j > 0:
                    pre = inf
                    for v in range(10):
                        if v != k:
                            pre = min(pre, dp[j - 1][v])
                    dp[j][k] += pre

        # print(dp)

        return min(dp[n - 1])
