#!/usr/bin/env python3


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
