#!/usr/bin/env python3


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                (
                    matrix[i][j],
                    matrix[n - 1 - j][i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[j][n - 1 - i],
                ) = (
                    matrix[n - 1 - j][i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[j][n - 1 - i],
                    matrix[i][j],
                )


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (i, j) -> (j, n-1-i)
        # => (i, j) - > (j, i) -> (j, n-1-i)

        n = len(matrix)

        # Step 1: 转置
        # (i, j) - > (j, i)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: 每行水平翻转
        # (j, i) -> (j, n-1-i)
        for row in matrix:
            row.reverse()
