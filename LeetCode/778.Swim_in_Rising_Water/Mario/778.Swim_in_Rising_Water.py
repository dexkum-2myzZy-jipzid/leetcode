#!/usr/bin/env python3


# Dijkstra
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


# dfs
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # val in grid is unique
        n = len(grid)

        res = inf
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        @cache
        def dfs(i, j, t):
            nonlocal res
            # cell no need to continue
            if (
                i < 0
                or i >= n
                or j < 0
                or j >= n
                or grid[i][j] == -1
                or grid[i][j] > res
            ):
                return inf

            if i == n - 1 and j == n - 1:
                max_val = max(t, grid[n - 1][n - 1])
                if max_val < res:
                    res = max_val
                return max_val

            val = grid[i][j]
            if val > t:
                t = val
            grid[i][j] = -1
            ans = inf
            for dx, dy in DIRS:
                nx, ny = i + dx, j + dy
                ans = min(dfs(nx, ny, t), ans)
            grid[i][j] = val
            return ans

        dfs(0, 0, 0)

        return res
