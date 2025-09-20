#!/usr/bin/env python3
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # build graph
        # graph: 'b': {'a': 0.5, 'c': 3.0},

        graph = defaultdict(dict)
        for arr, val in zip(equations, values):
            a, b = arr[0], arr[1]
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        # dfs a / c : a -> b -> c
        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0
            elif a == b:
                return 1.0

            visited.add(a)
            for c in graph[a]:
                if c in visited:
                    continue
                tmp = dfs(c, b, visited)
                if tmp != -1.0:
                    return graph[a][c] * tmp

            return -1.0

        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res
