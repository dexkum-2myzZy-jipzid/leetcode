#!/usr/bin/env python3


# my binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 0, n-1
        # x m y ->  ( x < m and m > y)  m is peak
        #  x > m and m > y
        # x < m and m < y
        nums = [-math.inf] + nums + [-math.inf]
        n = len(nums)
        l, r = 1, n - 1

        while l < r:
            m = (l + r) // 2

            # check if mth element is peak
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m - 1
            elif nums[m - 1] > nums[m] > nums[m + 1]:
                r = m
            elif nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:  # nums[m-1] > nums[m] and nums[m] < nums[m+1]
                l = m + 1

        return l - 1


# binary search
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left  # 或 return right，最后 left==right
