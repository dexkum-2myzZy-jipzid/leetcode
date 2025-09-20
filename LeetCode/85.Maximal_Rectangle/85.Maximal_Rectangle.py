#!/usr/bin/env python3


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        grid = []

        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            tmp = []
            for j, str1 in enumerate(row):
                if str1 == "0":
                    tmp.append(0)
                else:  # num is '1'
                    if i > 0 and grid[i - 1][j] > 0:
                        tmp.append(grid[i - 1][j] + 1)
                    else:
                        tmp.append(1)
            grid.append(tmp)

        # get largest rectangle by row 0 -> m-1
        res = 0
        for row in grid:
            height = [0] + row + [0]
            stack = []
            for i, num in enumerate(height):

                while stack and height[stack[-1]] > num:
                    h = height[stack.pop()]
                    left = stack[-1]
                    area = (i - left - 1) * h
                    res = max(res, area)

                stack.append(i)

        return res
