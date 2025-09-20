#!/usr/bin/env python3

import bisect


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # sorted array, exactly 2, only 1 elmenet once
        # return once element
        # [1,1,2,3,3,4,4,8,8] n = 9 left = 1, right = 8

        n = len(nums)
        if n == 1:
            return nums[0]

        left, right = nums[0], nums[-1] + 1
        while left < right:
            mid = (left + right) >> 1
            idx = bisect.bisect_left(nums, mid)
            if idx % 2 == 0:
                left = mid + 1
            else:
                right = mid

        return left - 1


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # sorted array, exactly 2, only 1 elmenet once
        # return once element
        # [1,1,2,3,3,4,4,8,8] n = 9 left = 1, right = 8

        n = len(nums)

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            # ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
