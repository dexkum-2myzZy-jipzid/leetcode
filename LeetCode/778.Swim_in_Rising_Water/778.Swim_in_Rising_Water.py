#!/usr/bin/env python3

import heapq
from typing import List
from math import inf
from collections import deque
from functools import cache


# Dijkstra
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijstra
        n = len(grid)

        times = [[inf] * n for _ in range(n)]

        heap = [(grid[0][0], 0, 0)]  # (t, r, c)
        times[0][0] = grid[0][0]

        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if t > times[r][c]:
                continue

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    nt = max(t, grid[nr][nc])
                    if nt < times[nr][nc]:
                        times[nr][nc] = nt
                        heapq.heappush(heap, (nt, nr, nc))

                        # print(f"nr:{nr} nc:{nc} grid:{grid[nr][nc]}")
                        # print(f"heap:{heap}")
                        # for row in times:
                        #     print(row)
                        # print()
        return inf


# binary search
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search
        n = len(grid)

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # bfs
        def can_reach(x):
            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])

            while q:
                i, j = q.popleft()

                if i == n - 1 and j == n - 1:
                    return True

                for dx, dy in DIRS:
                    nx, ny = i + dx, j + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and x >= grid[nx][ny]
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False

        # binary search
        left, right = max(grid[0][0], grid[n - 1][n - 1]), n * n - 1

        while left < right:
            mid = (left + right) // 2
            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left


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
