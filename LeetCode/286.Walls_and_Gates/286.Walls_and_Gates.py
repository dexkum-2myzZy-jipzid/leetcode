#!/usr/bin/env python3


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # m * n
        # -1 wall or obstacle
        # 0: gate
        # INF: empty

        INF = 2147483647
        DIRS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        m, n = len(rooms), len(rooms[0])

        # BFS
        q = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dis = 0
        while q:
            size = len(q)
            dis += 1
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == INF:
                        rooms[ni][nj] = dis
                        q.append((ni, nj))
