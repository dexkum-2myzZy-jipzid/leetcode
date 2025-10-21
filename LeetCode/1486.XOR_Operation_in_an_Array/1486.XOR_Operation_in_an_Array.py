#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # nums nums[i] = start + 2 * i

        # iterate index from 0 to n-1
        # based equation, i will get num = start + 2 * i
        # res ^= num

        res = 0

        for i in range(n):
            res ^= start + 2 * i

        return res
