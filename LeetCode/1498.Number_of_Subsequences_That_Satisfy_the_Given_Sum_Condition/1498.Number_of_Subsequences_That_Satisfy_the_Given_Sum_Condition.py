#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:

        MOD = 10**9 + 7

        n = len(nums)
        nums.sort()

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        res = 0
        for i, num in enumerate(nums):
            right = target - num
            # find idx which nums[idx] > right
            idx = bisect.bisect_right(nums, right) - 1
            if i <= idx < n:
                res = (res + pow2[idx - i]) % MOD

        return res


class Solution2:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        MOD = 10**9 + 7
        left, right = 0, n - 1
        res = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                contribution = pow(2, right - left, MOD)
                res = (res + contribution) % MOD
                left += 1
            else:
                right -= 1

        return res
