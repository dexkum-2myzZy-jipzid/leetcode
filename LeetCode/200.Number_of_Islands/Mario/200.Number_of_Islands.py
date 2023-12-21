#!/usr/bin/env python3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[True for _ in range(n)] for _ in range(m)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def findNextIsland(i, j):
            # handle out of edges
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            # handle visited:
            if not visited[i][j]:
                return
            else:
                visited[i][j] = False

            # find next island
            if grid[i][j] == "1":
                for a, b in directions:
                    findNextIsland(i+a, j+b)

        res = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] and grid[i][j] == "1":
                    res += 1
                    findNextIsland(i, j)

        return res
