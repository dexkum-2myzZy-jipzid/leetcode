#!/usr/bin/env python3


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # [x, y] -> [m, y+k]
        # j:[y, y + k]

        a, b = x, x + k - 1

        while a < b:

            for j in range(y, y + k):
                grid[a][j], grid[b][j] = grid[b][j], grid[a][j]

            a += 1
            b -= 1

        return grid
