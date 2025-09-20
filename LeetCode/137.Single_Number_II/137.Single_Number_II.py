#!/usr/bin/env python3


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # tc: O(n) / sc:O(1)
        res = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += num >> i & 1

            if bit_sum % 3:
                if i == 31:
                    res -= 1 << 31
                else:
                    res |= 1 << i
        return res
