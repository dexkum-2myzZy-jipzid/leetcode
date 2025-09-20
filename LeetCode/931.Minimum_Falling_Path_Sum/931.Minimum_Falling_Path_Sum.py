#!/usr/bin/env python3


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp = len(row)
        # dp[i] += min(matrix[row][i-1], matrix[row][i], matrix[row][i+1])

        m, n = len(matrix), len(matrix[0])

        # init
        dp = matrix[0][:]

        for i in range(1, m):
            new_dp = [0] * n
            for j in range(n):
                l, x, r = inf, inf, inf
                if j - 1 >= 0:
                    l = dp[j - 1]
                if j + 1 < n:
                    r = dp[j + 1]
                x = dp[j]

                new_dp[j] = matrix[i][j] + min(l, x, r)
            dp = new_dp

        # print(dp)

        return min(dp)
