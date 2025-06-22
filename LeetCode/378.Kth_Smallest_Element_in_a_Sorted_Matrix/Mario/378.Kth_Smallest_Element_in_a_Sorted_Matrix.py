#!/usr/bin/env python3


# binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_small_num(x):
            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, x)
            return count

        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            # check func to count how many val smaller than mid
            if count_small_num(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


# bfs
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # start: (0, 0), -> (0, 1) / (1,0)
        heap = []
        heap = [(matrix[0][0], 0, 0)]
        matrix[0][0] = -1

        while heap:
            cur, x, y = heapq.heappop(heap)

            k -= 1
            if k == 0:
                return cur

            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] != -1:
                    heapq.heappush(heap, (matrix[nx][ny], nx, ny))
                    matrix[nx][ny] = -1

        return 0
