#!/usr/bin/env python3

import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row is non-decreasing order
        # row[i][0] > row[i-1][-1]
        m, n = len(matrix), len(matrix[0])

        def get_idx(mid: int) -> tuple[int, int]:
            return (mid // n, mid % n)

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = get_idx(mid)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
