#!/usr/bin/env python3


# bfs
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # one island
        # cell connected boundary and water

        m, n = len(grid), len(grid[0])
        DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in DIRS:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m:
                            res += 1
                        if nj < 0 or nj >= n:
                            res += 1
                        if 0 <= ni < m and 0 <= nj < n:
                            if grid[ni][nj] == 0:
                                res += 1

        return res


# better count
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # one island
        # cell connected boundary and water

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4

                    # check left cell
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    # checl up cell
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2

        return res
