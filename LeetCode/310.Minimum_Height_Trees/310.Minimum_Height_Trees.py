#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        # build graph, degree,

        # if degree == 1, means leaf

        # from outer to inner

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque([i for i, deg in enumerate(degree) if deg == 1 or deg == 0])
        remain = n

        while remain > 2:
            size = len(q)
            remain -= size

            for _ in range(size):
                idx = q.popleft()
                for nei in graph[idx]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)
