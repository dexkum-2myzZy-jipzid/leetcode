#!/usr/bin/env python3


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # idx in [l,r] nums[idx] * v, idx += k

        n = len(nums)
        # prefix xor
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ nums[i]

        res = prefix[-1]

        # unchanged part: res ^ (prefix[r] ^ prefix[l])
        # change part: nums_xor[l:r]

        for q in queries:
            l, r, k, v = q
            for i in range(l, r + 1, k):
                res ^= nums[i]
                tmp = (nums[i] * v) % MOD
                nums[i] = tmp
                res ^= nums[i]

        return res
