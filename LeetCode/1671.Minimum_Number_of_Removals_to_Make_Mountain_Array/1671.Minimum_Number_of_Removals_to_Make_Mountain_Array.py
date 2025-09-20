#!/usr/bin/env python3


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # n - longest mountain array = min remove
        # [4,3,2,1,1,2,3,1]

        # every i th index, left LIS longest increasing array, right longest decreasing array
        # get 1 + len(left) + len(right)

        n = len(nums)

        # LIS
        left = [0] * n
        LIS = []
        for i in range(n):
            x = nums[i]
            idx = bisect.bisect_left(LIS, x)
            if idx == len(LIS):
                LIS.append(x)
            else:
                LIS[idx] = x
            left[i] = idx

        # LDS
        right = [0] * n
        LDS = []
        for i in range(n - 1, -1, -1):
            y = nums[i]
            idx = bisect.bisect_left(LDS, y)
            if idx == len(LDS):
                LDS.append(y)
            else:
                LDS[idx] = y
            right[i] = idx

        res = 1
        for i in range(1, n - 1):
            if left[i] and right[i]:
                res = max(res, 1 + left[i] + right[i])

        return n - res
