#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import List


# Reverse Topological Sort
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # terminal node <- safe node
        n = len(graph)

        outdegree = [len(graph[i]) for i in range(n)]

        grid = defaultdict(list)
        for i, neis in enumerate(graph):
            for nei in neis:
                grid[nei].append(i)

        q = deque([])
        for i, v in enumerate(outdegree):
            if v == 0:
                q.append(i)

        while q:
            i = q.popleft()
            for nei in grid[i]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    q.append(nei)

        return [i for i, v in enumerate(outdegree) if v == 0]


# dfs
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0 unvisited, 1 visiting, 2 safe

        def dfs(i):
            if state[i] > 0:
                return state[i] == 2
            state[i] = 1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            state[i] = 2
            return True

        return [i for i in range(n) if dfs(i)]
