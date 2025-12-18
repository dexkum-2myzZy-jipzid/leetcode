#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        f1, f2 = 0, 1
        for i in range(2, n + 1):
            cur = f1 + f2
            f1, f2 = f2, cur

        return f2
