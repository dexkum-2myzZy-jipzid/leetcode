#!/usr/bin/env python3


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        n = len(nums)
        res = math.inf
        l, cur = 0, 0

        for r, v in enumerate(nums):
            cur += v
            while l <= r and cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1

        return 0 if res == math.inf else res
