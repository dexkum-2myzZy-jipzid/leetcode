#!/usr/bin/env python3

import heapq
from math import inf


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # Dijkstra
        # efforts[i][j] represent mini effort required from (0,0) to (i, j)

        m, n = len(heights), len(heights[0])
        efforts = [[inf] * n for _ in range(m)]

        heap = [(0, 0, 0)]  # (i, j)

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            curr, i, j = heapq.heappop(heap)

            if curr > efforts[i][j]:
                continue

            # reach bottom-right cell
            if i == m - 1 and j == n - 1:
                return curr

            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n:
                    abs_dis = abs(heights[i][j] - heights[ni][nj])
                    effort = max(abs_dis, curr)
                    if effort < efforts[ni][nj]:
                        efforts[ni][nj] = effort
                        heapq.heappush(heap, (effort, ni, nj))

        return int(efforts[m - 1][n - 1])


# binary search with dfs
class Solution2:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        # binary search to find min effort
        # left = 0, right = max(heights) - min(heights)
        # function can_reach_bottom_right(mid)

        m, n = len(heights), len(heights[0])

        DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def can_reach(mid: int) -> bool:
            stack = []
            seen = [[False] * n for _ in range(m)]
            stack.append((0, 0))
            seen[0][0] = True

            while stack:
                i, j = stack.pop()

                if i == m - 1 and j == n - 1:
                    return True

                cur = heights[i][j]

                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj]:
                        next_height = heights[ni][nj]
                        abs_dis = abs(next_height - cur)
                        if abs_dis <= mid:
                            seen[ni][nj] = True
                            stack.append((ni, nj))

            return False

        left, right = 0, 10**6

        res = 10**6
        while left < right:
            mid = (left + right) // 2
            if can_reach(mid):
                res = mid
                right = mid
            else:
                left = mid + 1

        return res
