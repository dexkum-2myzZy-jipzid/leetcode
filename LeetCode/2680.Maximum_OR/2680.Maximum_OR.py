#!/usr/bin/env python3


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] | nums[i - 1]

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]

        res = 0
        for i, num in enumerate(nums):
            res = max(res, prefix[i] | (num << k) | suffix[i + 1])

        return res
