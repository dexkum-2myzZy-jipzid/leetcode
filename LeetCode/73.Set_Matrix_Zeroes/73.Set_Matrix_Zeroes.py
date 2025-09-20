#!/usr/bin/env python3


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # ✅ 判断是否第一行或第一列需要清零
        first_row_zero = any(matrix[0][i] == 0 for i in range(n))
        first_column_zero = any(matrix[i][0] == 0 for i in range(m))

        # ✅ 标记过程，从 (1,1) 开始，避免污染第一行/列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # ✅ 设置矩阵中非第一行/列的元素
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # ✅ 根据记录单独处理第一行
        if first_row_zero:
            for i in range(n):
                matrix[0][i] = 0

        # ✅ 根据记录单独处理第一列
        if first_column_zero:
            for i in range(m):
                matrix[i][0] = 0
