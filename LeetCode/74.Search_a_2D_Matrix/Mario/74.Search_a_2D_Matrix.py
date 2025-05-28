#!/usr/bin/env python3


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i = 0
        while i < m:
            cur = matrix[i]
            index = bisect.bisect_left(cur, target)
            if index == n:
                i += 1
            elif cur[index] == target:
                return True
            else:
                return False

        return False
