#!/usr/bin/env python3


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # topological sort
        n, m = len(colors), len(edges)

        # init dp[i][c], reach i,the max count of color c
        dp = [[0] * 26 for _ in range(n)]
        # create graph, indegree arry
        indegree = [0] * n
        graph = defaultdict(list)
        for e in edges:
            a, b = e
            graph[a].append(b)
            indegree[b] += 1

        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
            dp[i][ord(colors[i]) - ord("a")] = 1

        res = 0
        vis = 0

        while q:
            v = q.popleft()
            vis += 1

            for nei in graph[v]:

                for c in range(26):
                    tmp = dp[v][c]
                    if c == (ord(colors[nei]) - ord("a")):
                        tmp += 1
                    dp[nei][c] = max(dp[nei][c], tmp)

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res = max(res, max(dp[v]))

        return res if vis == n else -1
