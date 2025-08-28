#!/usr/bin/env python3

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # print(heap)
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = 0
        while heap:
            water_level, i, j = heapq.heappop(heap)

            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:

                    nei_water_level = max(heightMap[ni][nj], water_level)

                    res += nei_water_level - heightMap[ni][nj]

                    visited[ni][nj] = True
                    heapq.heappush(heap, (nei_water_level, ni, nj))

        return res
