#!/usr/bin/env python3


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[y] > self.size[x]:
            rx, ry = ry, rx
        self.size[rx] += self.size[ry]
        self.parent[ry] = rx
        return True


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        #  0
        # 1 2
        #  3
        # " " connect (0, 1, 2, 3)
        # '/' connect (0,1), (2,3)
        # "\" connect (0, 2),(1,3)

        n = len(grid)
        uf = UnionFind(4 * n * n)

        for i in range(n):
            for j in range(n):
                k = (i * n + j) * 4

                if grid[i][j] == " ":
                    uf.union(k + 0, k + 1)
                    uf.union(k + 2, k + 3)
                    uf.union(k + 0, k + 2)
                elif grid[i][j] == "/":
                    uf.union(k + 0, k + 1)
                    uf.union(k + 2, k + 3)
                elif grid[i][j] == "\\":
                    uf.union(k + 0, k + 2)
                    uf.union(k + 1, k + 3)

                # connect cell below
                if i + 1 < n:
                    uf.union(k + 3, (i + 1) * n * 4 + j * 4)

                # connect cell right
                if j + 1 < n:
                    uf.union(k + 2, i * n * 4 + (j + 1) * 4 + 1)

        res = sum(uf.find(x) == x for x in range(n * n * 4))
        return res
