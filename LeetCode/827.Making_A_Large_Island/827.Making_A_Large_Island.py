#!/usr/bin/env python3


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)  # [1, 500]

        def get_index(i, j):
            return i * n + j

        # connect 1 cell (union find)
        total = n * n
        parent = list(range(total))
        size = [1] * total

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return

            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            union(get_index(x, y), get_index(nx, ny))
                else:
                    size[get_index(x, y)] = 0

        # print(parent)
        # print(size)

        # iterate cell which contains 0
        res = max(size)
        for x in range(n):
            for y in range(n):
                # if we change 0 to be 1, the biggest size of island we can get
                if grid[x][y] == 0:
                    nei = 1  # 0 cell connect island area
                    vis = set()  # put parent index in vis to avoid duplicate
                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            root = find(get_index(nx, ny))
                            if root not in vis:
                                nei += size[root]
                                vis.add(root)

                    res = max(res, nei)

        return res
