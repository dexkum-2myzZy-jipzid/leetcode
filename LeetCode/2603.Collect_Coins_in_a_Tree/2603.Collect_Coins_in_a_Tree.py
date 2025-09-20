#!/usr/bin/env python3

from collections import defaultdict, deque


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # Special case: If there are no coins at all, no operation is needed.
        if sum(coins) == 0:
            return 0

        n = len(coins)
        degree = [0] * n
        graph = defaultdict(list)
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)
            degree[u] += 1
            degree[v] += 1

        # Step 1: Remove all leaves (degree == 1) that do not have a coin.
        q = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)

        while q:
            v = q.popleft()
            degree[v] = 0  # Mark this node as removed
            for nei in graph[v]:
                if degree[nei] > 0:
                    degree[nei] -= 1
                    if degree[nei] == 1 and coins[nei] == 0:
                        q.append(nei)

        # Step 2: Remove all current leaves for two rounds (regardless of coins)
        for _ in range(2):
            q = deque()
            for i in range(n):
                if degree[i] == 1:
                    q.append(i)
            while q:
                v = q.popleft()
                degree[v] = 0  # Mark this node as removed
                for nei in graph[v]:
                    if degree[nei] > 0:
                        degree[nei] -= 1

        # Step 3: The remaining degrees represent the remaining edges (each edge is counted twice).
        # The answer is the sum of degrees (number of edges times 2).
        return max(sum(degree), 0)
