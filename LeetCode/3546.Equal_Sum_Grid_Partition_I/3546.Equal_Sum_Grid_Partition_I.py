#!/usr/bin/env python3


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(x) for x in grid])
        if total % 2 == 1:
            return False

        def helper(m):
            arr = [sum(x) for x in m]
            half = total // 2
            cur = 0
            for x in arr:
                cur += x
                if cur == half:
                    return True
                elif cur > half:
                    return False
            return False

        return helper(grid) or helper(list(zip(*grid)))
