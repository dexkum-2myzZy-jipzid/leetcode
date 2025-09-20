#!/usr/bin/env python3


# dfs
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[0])

        # i represent ith row, j represent jth column
        @cache
        def dfs(i, j):
            if i == m:
                return 0

            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]

        return dfs(0, 0)


# dp
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # init
        dp = triangle[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]
