#!/usr/bin/env python3


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        res = max_dp = min_dp = nums[0]

        for i in range(1, n):
            num = nums[i]
            if num >= 0:
                max_dp, min_dp = max(max_dp * num, num), min(min_dp * num, num)
            else:
                max_dp, min_dp = max(min_dp * num, num), min(max_dp * num, num)

            res = max(res, max_dp)

        return res
