#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1
