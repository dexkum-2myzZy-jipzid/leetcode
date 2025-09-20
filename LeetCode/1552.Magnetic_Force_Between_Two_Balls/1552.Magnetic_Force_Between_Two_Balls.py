#!/usr/bin/env python3


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # magnetic force = abs(x-y)
        n = len(position)
        # sort position
        position.sort()

        def helper(x):
            cnt = 1
            pre = position[0]
            for i in range(1, n):
                if position[i] - pre >= x:
                    cnt += 1
                    pre = position[i]
                if cnt >= m:
                    return True
            return False

        # binary search
        left, right = 1, position[-1] - position[0] + 1
        res = 0
        while left < right:
            mid = (left + right) >> 1
            if helper(mid):
                res = mid
                left = mid + 1
            else:
                right = mid

        return res
