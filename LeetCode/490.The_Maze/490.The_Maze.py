#!/usr/bin/env python3


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        # bfs input i, j
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # mark -1 if visited

        m, n = len(maze), len(maze[0])  # [1, 100]
        [i, j] = start
        vis = set((i, j))
        q = deque([(i, j)])

        while q:
            i, j = q.popleft()
            if [i, j] == destination:
                return True

            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == 0:
                    while (
                        0 <= ni + di < m
                        and 0 <= nj + dj < n
                        and maze[ni + di][nj + dj] == 0
                    ):
                        ni += di
                        nj += dj

                    if (ni, nj) not in vis:
                        vis.add((ni, nj))
                        q.append((ni, nj))

        return False
