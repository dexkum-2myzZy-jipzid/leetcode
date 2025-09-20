#!/usr/bin/env python3


class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        # a < b
        # build graph
        graph = defaultdict(list)

        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        n = len(edges) + 1
        res = [0] * n

        @cache
        def dfs(parent, cur, weight):
            cnt = 1 if weight % signalSpeed == 0 else 0
            for nei, neiw in graph[cur]:
                if nei == parent:
                    continue
                else:
                    cnt += dfs(cur, nei, (weight + neiw) % signalSpeed)
            return cnt

        for i in range(n):
            neis = graph[i]
            m = len(neis)
            cnt = 0
            for j in range(m):
                a, aw = neis[j]
                for k in range(j + 1, m):
                    b, bw = neis[k]
                    cnt += dfs(i, a, aw % signalSpeed) * dfs(i, b, bw % signalSpeed)
            res[i] = cnt

        return res
