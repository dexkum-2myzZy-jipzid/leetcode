#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # half-open interval [left, right)
        # invariant: if target exists, it's in nums[left:right]
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


class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        # closed interval [left, right]
        # invariant: if target exists, it's in nums[left:right+1]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# ...existing code...
