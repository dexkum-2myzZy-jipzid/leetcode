#!/usr/bin/env python3


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Every vertex pair is connected by at most one edge

        # convert edges to graph, adjacency list
        graph = defaultdict(list)
        for e in edges:
            u, v = e
            graph[u].append(v)
            graph[v].append(u)

        MAXN = 1001
        res = MAXN
        for i in range(n):
            dis = [MAXN] * n
            parent = [-1] * n
            q = deque([i])
            dis[i] = 0

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dis[v] == MAXN:
                        dis[v] = dis[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        res = min(res, dis[u] + dis[v] + 1)

        return res if res != MAXN else -1
