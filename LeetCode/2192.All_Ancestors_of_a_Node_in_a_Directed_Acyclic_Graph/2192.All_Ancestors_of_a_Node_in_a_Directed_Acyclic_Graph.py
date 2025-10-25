#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # graph child:[parents]

        # dfs(child) -> parents

        res = []
        graph = defaultdict(list)
        for f, t in edges:
            graph[t].append(f)

        @cache
        def dfs(node: int) -> list[int]:
            if node not in graph:
                return []

            parents = graph[node]
            res = set()
            for p in parents:
                res.add(p)
                res |= set(dfs(p))

            return sorted(list(res))

        for i in range(n):
            res.append(dfs(i))

        return res


# topological sort
from collections import deque, defaultdict


class Solution2:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:

        # topological sort

        graph = defaultdict(list)
        indegree = [0] * n

        # u -> v, u is ancestor
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        ancestors = [set() for _ in range(n)]

        while q:
            u = q.popleft()

            for v in graph[u]:

                if ancestors[u]:
                    ancestors[v].update(ancestors[u])
                ancestors[v].add(u)

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [sorted(list(s)) for s in ancestors]
