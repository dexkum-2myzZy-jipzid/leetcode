#!/usr/bin/env python3


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0  # count 0s in the subarray
        res = 0  #

        for num in nums:
            if num == 0:
                cnt += 1
            else:
                res += (cnt + 1) * cnt // 2
                cnt = 0
        res += (cnt + 1) * cnt // 2
        return res
