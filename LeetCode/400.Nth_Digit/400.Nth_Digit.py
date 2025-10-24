#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findNthDigit(self, n: int) -> int:

        # 1-9  9*1 k = 1
        # 10-99 9 * 10 = 90 * 2 = 180 = 90 * 2
        # 100-999 9 * 10 * 10 = 900 * 3 = 2700 = 900 * 3
        # 9 * k * 10 ^ (k-1)

        k = 1
        base = 1
        while n > 0:
            count = 9 * k * base
            # n in [k-1, k]
            if n > count:
                n -= count
                k += 1
                base *= 10
            else:
                break

        if k == 1:
            return n

        # n = 2, k = 2
        num_offset, digit_offset = divmod(n - 1, k)
        num = base + num_offset

        # print(num, digit_offset, k)

        return int(str(num)[digit_offset])
