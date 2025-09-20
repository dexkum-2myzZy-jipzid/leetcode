#!/usr/bin/env python3


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k = len(mat1), len(mat2[0]), len(mat2)

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for kk in range(k):
                if mat1[i][kk] != 0:
                    for j in range(n):
                        res[i][j] += mat1[i][kk] * mat2[kk][j]

        return res
