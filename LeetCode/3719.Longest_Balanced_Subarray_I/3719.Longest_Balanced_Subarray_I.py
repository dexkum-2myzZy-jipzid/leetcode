#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        # balanced, len(set(even)) == len(set(odd))
        # return longest subarr

        n = len(nums)
        res = 0
        for i in range(n):
            odd, even = set(), set()
            for j in range(i, n):
                num = nums[j]
                if num % 2 == 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])

                odd_len, even_len = len(odd), len(even)

                if (
                    odd_len > 0
                    and even_len > 0
                    and odd_len == even_len
                    and j - i + 1 > res
                ):
                    res = j - i + 1

        return res
