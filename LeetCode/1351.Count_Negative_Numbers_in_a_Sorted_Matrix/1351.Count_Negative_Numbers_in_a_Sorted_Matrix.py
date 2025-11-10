#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        # 4,3,2,-1
        # 3,2,1,-1
        # 1,1,-1,-2
        # -1,-1,-2,-3

        # from (0, n-1), if grid[r][c] < 0, means current col all < 0, then c -= 1
        # if grid[r][c] >= 0, means check r+= 1

        m, n = len(grid), len(grid[0])

        row, col = 0, n - 1
        res = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                res += m - row
                col -= 1
            else:
                row += 1

        return res
