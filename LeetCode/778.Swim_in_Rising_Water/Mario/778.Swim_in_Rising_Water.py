#!/usr/bin/env python3


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra algo
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = inf

        while heap:
            t, i, j = heapq.heappop(heap)

            if i == n - 1 and j == n - 1:
                if t < res:
                    res = t
                continue

            # no need to continue
            if res != inf and t >= res:
                continue

            for dx, dy in DIRS:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:
                    nxt_t = max(grid[nx][ny], t)
                    grid[nx][ny] = -1
                    heapq.heappush(heap, (nxt_t, nx, ny))

        return res
