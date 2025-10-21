#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        # preprocess this nums, know increasing subarrang range
        # e.g. [2,5,7,8,9,2,3,4,3,1] => [0, 4][5, 7]
        # there are 2 increasing subarray

        # first, one pass, to get intervals
        nums += [-1001]
        n = len(nums)
        l = 0
        intervals = []
        for r in range(1, n):
            if nums[r] <= nums[r - 1]:
                if r - l >= k:
                    intervals.append((l, r - 1))
                l = r

        # print(intervals)

        # then check whether there exist two adjacent subarrays of at least length k
        # 2 test cases:
        # 1. len(intervals) >= 2*k, means two adjacent subarrays
        # 2. exist 2 subarray, intervals[i][1] + 1 == intervals[i][0]

        m = len(intervals)
        for i, (s, e) in enumerate(intervals):
            if (e - s + 1) >= 2 * k:
                return True
            elif i < m - 1:
                next_interval = intervals[i + 1]
                if e + 1 == next_interval[0]:
                    return True

        return False
