#!/usr/bin/env python3


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums[i] * nums[j] is max
        # return product of pair, if not, return 0

        # nums.sort()
        n = len(nums)

        # print(nums)
        # a, b  max(a * b) and a & b == 0

        B = max(nums).bit_length()
        LIMIT = 1 << B

        dp = [0] * LIMIT
        for num in nums:
            dp[num] = max(dp[num], num)

        # print(dp)
        for i in range(B):
            half = 1 << i
            step = half << 1
            for base in range(0, LIMIT, step):
                lo = base + half
                hi = min(base + step, LIMIT)
                j = lo
                k = lo - half
                dpl = dp
                while j < hi:
                    v = dpl[k]
                    if v > dpl[j]:
                        dpl[j] = v
                    j += 1
                    k += 1

        res = 0
        for num in set(nums):
            comp = (LIMIT - 1) ^ num
            p = dp[comp]
            if p:
                res = max(res, num * p)
        return res
