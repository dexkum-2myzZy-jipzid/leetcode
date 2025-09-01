#!/usr/bin/env python3


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = nums

        res, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
                if cnt > res:
                    res = cnt
            else:
                cnt = 0

        return res
