#!/usr/bin/env python3


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        # 4 -> [1, 3], [5]
        # 2 -> [1] [3] [5]

        #  [1, 2, 3]
        # 0 1 1 1

        n = len(arr)
        if n == m:
            return n

        length = [0] * (n + 2)

        count_m = 0
        res = -1
        for i, pos in enumerate(arr):
            left, right = length[pos - 1], length[pos + 1]
            total = left + right + 1
            # update boundaries of interval
            length[pos - left] = length[pos + right] = total

            # update count of length m interval
            if left == m:
                count_m -= 1
            if right == m:
                count_m -= 1

            if total == m:
                count_m += 1
            if count_m > 0:
                res = i + 1

        return res
