#!/usr/bin/env python3


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # get degree graph
        roads_set = set()
        degree = [0] * n
        for v, u in roads:
            degree[u] += 1
            degree[v] += 1
            roads_set.add((v, u))
            roads_set.add((u, v))

        # one pass roads, count network rank,get max network rank
        res = -inf
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in roads_set:
                    rank -= 1
                res = max(res, rank)

        return res
