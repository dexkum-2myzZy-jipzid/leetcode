#!/usr/bin/env python3


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # sorted unique
        # inclusive
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i
            cur = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if i > j:
                s = str(nums[j]) + "->" + str(nums[i])
                res.append(s)
            elif i == j:
                res.append(str(nums[j]))
            i += 1

        return res
