#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def totalMoney(self, n: int) -> int:

        # Mon T W T F S Sun
        # 1   2 3 4 5 6 7.    sum(array) = 28
        # 2   3 ...           28 + 7 = 35

        weeks, days = divmod(n, 7)

        mon, i = 1, 0
        res = 0
        while i < weeks:
            res += 28 + i * 7
            i += 1
            mon += 1

        for i in range(days):
            res += mon + i

        return res
