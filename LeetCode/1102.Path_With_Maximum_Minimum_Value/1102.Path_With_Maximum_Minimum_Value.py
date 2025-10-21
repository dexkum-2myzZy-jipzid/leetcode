#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        # m * n matrix
        m, n = len(grid), len(grid[0])

        # Dijistra from (0, 0), push (-score, i, j) into heap, this max heap
        seen = [[False] * n for _ in range(m)]
        heap = []
        heapq.heappush(heap, (-grid[0][0], 0, 0))
        seen[0][0] = True

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # pop out element, iterate its 4 directions, if new (i, j) not visited,
        while heap:
            cur_score, i, j = heapq.heappop(heap)
            cur_score = -cur_score

            if i == m - 1 and j == n - 1:
                return cur_score

            for di, dj in dirs:
                ni, nj = di + i, dj + j
                # check its boundary and visited or not
                # push new elmenet into heap, min(-score, next_i, next_j)
                if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj]:
                    seen[ni][nj] = True
                    min_score = min(cur_score, grid[ni][nj])
                    heapq.heappush(heap, (-min_score, ni, nj))

        return -1
