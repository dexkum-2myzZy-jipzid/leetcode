#!/usr/bin/env python3

import bisect


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        l, r = 0, n

        res = []
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if l < n and nums[l] == target:
            res.append(l)
        else:
            return [-1, -1]

        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m
            else:
                l = m + 1

        res.append(l - 1)
        return res


class Solution2:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = bisect.bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = bisect.bisect_right(nums, target)
        return [start, end - 1]
