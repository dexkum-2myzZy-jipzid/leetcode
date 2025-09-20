#!/usr/bin/env python3


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # use union find
        uf = UnionFind(n)

        for i in range(n - 1):
            j = i + 1
            if nums[j] - nums[i] <= maxDiff:
                uf.union(i, j)

        res = []
        for q in queries:
            u, v = min(q), max(q)
            if uf.find(u) == uf.find(v):
                res.append(True)
            else:
                res.append(False)

        return res


# another solution: group
class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        group = [0] * n
        cur_group = 0

        for i in range(n - 1):
            if nums[i + 1] - nums[i] > maxDiff:
                cur_group += 1
            group[i + 1] = cur_group

        res = []
        for q in queries:
            u, v = q[0], q[1]
            res.append(group[u] == group[v])

        return res
