#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        # (0, 0) -> (m-1, n-1) eliminate at most k obstacles

        # bfs, queue push element (steps, i, j, k)

        # if (i, j) == (m-1, n-1), return step

        # else iterate 4 directions, check next_step

        # e.g. 1. (ni, nj) in boundary,
        # 2. is obstacles, k > 0, so continue, k-1
        # 3. visited (steps, i, j, k) before or not

        m, n = len(grid), len(grid[0])

        first: tuple[int, int, int] = (0, 0, k)
        queue: deque[tuple[int, int, int]] = deque([first])
        seen: set[tuple[int, int, int]] = {first}

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        step = 0

        while queue:
            for _ in range(len(queue)):
                i, j, kk = queue.popleft()

                if (i, j) == (m - 1, n - 1):
                    return step

                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < m and 0 <= nj < n:
                        if (
                            grid[ni][nj] == 1
                            and kk > 0
                            and (ni, nj, kk - 1) not in seen
                        ):
                            seen.add((ni, nj, kk - 1))
                            queue.append((ni, nj, kk - 1))
                        elif grid[ni][nj] == 0 and (ni, nj, kk) not in seen:
                            seen.add((ni, nj, kk))
                            queue.append((ni, nj, kk))

            step += 1

        return -1


# more clever way to do visit
class Solution2:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])

        first: tuple[int, int, int] = (0, 0, k)
        queue: deque[tuple[int, int, int]] = deque([first])
        best = [[-1] * n for _ in range(m)]
        best[0][0] = k

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        step = 0

        while queue:
            for _ in range(len(queue)):
                i, j, kk = queue.popleft()

                if (i, j) == (m - 1, n - 1):
                    return step

                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < m and 0 <= nj < n:
                        rk = kk - grid[ni][nj]
                        if rk < 0:
                            continue

                        if rk > best[ni][nj]:
                            best[ni][nj] = rk
                            queue.append((ni, nj, rk))

            step += 1

        return -1
