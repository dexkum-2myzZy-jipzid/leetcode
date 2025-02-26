#!/usr/bin/env python3

"""
bfs tc: O(m*n)  sc: O(m*n)
dfs tc: O(m*n)  sc: O(m*n)
union-find tc: O(m*n)  sc: O(m*n)
"""


# bfs:

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        # directions
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque([(i, j)])

            grid[i][j] = "0"

            while queue:
                y, x = queue.popleft()
                for dy, dx in dirs:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == "1":
                        queue.append([ny, nx])
                        grid[ny][nx] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count


# dfs:

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        count = 0
        # directions
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for dy, dx in dirs:
                ny, nx = dy + i, dx + j
                dfs(ny, nx)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


# union-find


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        count = m * n
        total_land = sum(grid[i][j] == "1" for i in range(m) for j in range(n))
        uf = UnionFind(count, total_land)

        def index(i, j):
            return i * n + j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cur = index(i, j)
                    for dy, dx in [(1, 0), (0, 1)]:
                        ny, nx = i + dy, j + dx
                        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == "1":
                            uf.union(cur, index(ny, nx))

        return uf.count


class UnionFind:
    def __init__(self, n, total_land):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = total_land

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1