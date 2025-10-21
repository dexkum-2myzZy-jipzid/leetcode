#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # get the num of rows and the num of cols from matrix
        m, n = len(matrix), len(matrix[0])

        # create new matrix, we call it res, which hold final answer
        res = [[0] * m for _ in range(n)]

        # the key of transpose is res[i][j] = matrix[j][i]

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]

        return res
