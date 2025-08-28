#!/usr/bin/env python3

import heapq
from typing import List
from math import inf


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # heap (effort, i, j)

        m, n = len(heights), len(heights[0])

        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        efforts = [[inf] * n for _ in range(m)]

        # init max effort
        res = inf

        heap = [(0, 0, 0)]

        while heap:
            effort, i, j = heapq.heappop(heap)

            if effort > efforts[i][j]:
                continue

            if i == m - 1 and j == n - 1:
                return effort

            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    diff = abs(heights[ni][nj] - heights[i][j])
                    next_effort = max(diff, effort)
                    if next_effort < efforts[ni][nj]:
                        efforts[ni][nj] = next_effort
                        heapq.heappush(heap, (next_effort, ni, nj))

                        # print(f"ni:{ni} nj:{nj} height:{heights[ni][nj]}")
                        # print(f"heap:{heap}")
                        # for r in efforts:
                        #     print(r)
                        # print()

        return 0
