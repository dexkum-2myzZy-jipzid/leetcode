#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True


class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:

        # union find, when earliest time every person became in one group, so this time is answer
        logs.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        cnt = n - 1
        for t, x, y in logs:
            ans = uf.union(x, y)
            if ans:
                cnt -= 1
            if cnt == 0:
                return t

        return -1
