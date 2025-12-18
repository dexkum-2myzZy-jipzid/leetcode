#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t3 = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t3

        return t2
