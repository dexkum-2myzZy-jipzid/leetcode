#!/usr/bin/env python3

# MST Minimum Spanning Tree


# MST Prim algo
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        n cities [1, n]
        bidirectional
        min cost / impossible -1

        prim algo
        min_dis = [inf] * n
        """

        min_dis = [inf] * (n + 1)

        # graph
        graph = defaultdict(list)
        for v1, v2, w in connections:
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))

        # start with city labed as 1
        heap = [(0, 1)]  # weight, node
        vis = set()
        res = 0

        while heap:
            w, v = heapq.heappop(heap)

            if v in vis:
                continue
            vis.add(v)
            res += w

            for v1, w1 in graph[v]:
                if v1 not in vis:
                    if w1 < min_dis[v1]:
                        heapq.heappush(heap, (w1, v1))

        if len(vis) < n:
            return -1
        return res


# Kruskal
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True

        # mst
        count = 0
        res = 0

        connections.sort(key=lambda x: x[2])

        for a, b, w in connections:
            if union(a, b):
                count += 1
                res += w

        return res if count == n - 1 else -1
