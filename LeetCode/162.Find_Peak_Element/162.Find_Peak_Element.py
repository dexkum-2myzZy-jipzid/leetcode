#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # nums[i-1] nums[i] nums[i+1]
        # if nums[i-1] < nums[i] > nums[i+1]:
        #     return nums[i]
        # elif nums[i-1] < nums[i] < nums[i+1]:
        #     left = i + 1
        # elif nums[i-1] > nums[i] > nums[i+1]:
        #     right = i -1
        # elif nums[i-1] > nums[i] < nums[i+1]:
        #     right = i - 1

        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2

            low = nums[mid - 1] if mid > 0 else -inf
            high = nums[mid + 1] if mid < n - 1 else -inf

            if low < nums[mid] and nums[mid] > high:
                return mid
            elif low < nums[mid] and nums[mid] < high:
                left = mid + 1
            elif low > nums[mid] and nums[mid] > high:
                right = mid - 1
            else:
                right = mid - 1

        return left


# binary search
class Solution2:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
