#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import lcm


class Solution:
    def minimumTime(self, d: list[int], r: list[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        rr = lcm(r1, r2)

        def helper(m: int) -> bool:
            a, b = m - m // r1, m - m // r2
            c = m - m // rr
            return a >= d1 and b >= d2 and (d1 + d2) <= c

        left, right = d1 + d2, d1 + d2

        while not helper(right):
            right *= 2

        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1

        return left
