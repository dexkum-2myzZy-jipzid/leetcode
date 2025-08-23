#!/usr/bin/env python3


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:

        def build_graph(n, edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def get_distance(graph, i, k):
            n = len(graph)
            vis = set([i])
            q = deque([(0, i)])
            cnt = 0
            while q:
                d, i = q.popleft()
                if d > k:
                    break
                else:
                    cnt += 1

                for v in graph[i]:
                    if v not in vis:
                        vis.add(v)
                        q.append([d + 1, v])

            return cnt

        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = build_graph(n, edges1)
        tree2 = build_graph(n, edges2)

        t1 = []
        for i in range(n):
            t1.append(get_distance(tree1, i, k))

        t2 = []
        for i in range(m):
            t2.append(get_distance(tree2, i, k - 1))

        max_t2 = max(t2) if t2 else 0

        res = []
        for i in range(n):
            res.append(t1[i] + max_t2)

        return res
