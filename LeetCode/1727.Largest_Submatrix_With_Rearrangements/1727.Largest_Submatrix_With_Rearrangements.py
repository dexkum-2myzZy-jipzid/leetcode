#!/usr/bin/env python3


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        # for r in matrix:
        #     print(sorted(r, reverse=True))

        res = 0
        for r in matrix:
            heights = sorted(r, reverse=True)
            for k, h in enumerate(heights):
                res = max(res, h * (k + 1))

        return res
