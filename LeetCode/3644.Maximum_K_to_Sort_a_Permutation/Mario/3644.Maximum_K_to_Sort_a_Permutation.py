#!/usr/bin/env python3


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1  # all 1 for binary
        flag = True
        for i in range(len(nums)):
            if nums[i] != i:
                flag = False
                k = k & nums[i] & i  # eliminate impossible 1 for binary
        if flag:
            return 0
        return k
