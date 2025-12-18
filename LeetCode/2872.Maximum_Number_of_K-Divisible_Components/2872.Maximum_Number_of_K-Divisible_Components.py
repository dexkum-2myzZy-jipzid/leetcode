#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        # dfs node
        # if current node with left & right node is divisible by k, increment result by 1

        # 1. build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = 0

        def dfs(node: int, parent: int) -> int:
            nonlocal res

            cur = values[node]
            for nei in graph[node]:
                if nei != parent:
                    cur += dfs(nei, node)

            if cur % k == 0:
                res += 1
                return 0
            else:
                return cur

        dfs(0, -1)

        return res
