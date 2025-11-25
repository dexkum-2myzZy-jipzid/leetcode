#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        # equal count of even and odd numbers
        # prefix diff

        prefix_xor, balance = 0, 0
        state = {(prefix_xor, balance): -1}
        res = 0

        for i, num in enumerate(nums):

            prefix_xor ^= num
            balance += 1 if num % 2 == 0 else -1
            curr = (prefix_xor, balance)

            if curr in state:
                res = max(res, i - state[curr])
            else:
                state[curr] = i

        return res
