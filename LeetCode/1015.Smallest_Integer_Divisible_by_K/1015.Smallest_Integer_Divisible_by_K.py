#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # num % k = 0
        # num only contains digit 1

        # a = 1 % k
        # b = (a * 10 + 1) % k = ((a % k) * 10 + 1) % k

        if k == 2 or k == 5:
            return -1

        remainder = 0
        for length in range(1, k + 1):

            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1
