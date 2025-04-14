#!/usr/bin/env python3


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = [[0] * n for _ in range(m)]

        # Calculate the longest increasing path starting from cell (i, j)
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            maxPath = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                    maxPath = max(maxPath, dfs(ni, nj) + 1)

            dp[i][j] = maxPath

            return dp[i][j]

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
