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
