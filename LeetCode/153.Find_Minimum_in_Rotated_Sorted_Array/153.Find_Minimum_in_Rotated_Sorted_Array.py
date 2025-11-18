#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]


class Solution2:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
