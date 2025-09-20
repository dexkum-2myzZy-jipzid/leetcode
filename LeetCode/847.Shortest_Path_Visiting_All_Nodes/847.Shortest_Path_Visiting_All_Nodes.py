#!/usr/bin/env python3


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # shortest path that visit every node
        # backtrack
        # visit unvisit node first, then if no other node, visit go back

        n = len(graph)
        if n == 1:
            return 0

        visited = [[False] * (1 << n) for _ in range(n)]
        q = deque([])

        # push all node into queue
        for i in range(n):
            mask = 1 << i
            visited[i][mask] = True
            q.append((i, mask, 0))  # i, mask, path

        while q:
            i, mask, path = q.popleft()

            if mask == (1 << n) - 1:
                return path

            for j in graph[i]:
                next_mask = mask | (1 << j)
                if not visited[j][next_mask]:
                    visited[j][next_mask] = True
                    q.append((j, next_mask, path + 1))

        return -1
