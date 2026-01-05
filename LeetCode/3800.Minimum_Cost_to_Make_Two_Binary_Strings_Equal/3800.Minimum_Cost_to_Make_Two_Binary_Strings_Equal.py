#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def minimumCost(
        self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int
    ) -> int:
        # i : s[i] or t[i]. cost:flipCost
        # i, j: s[i] s[j] or t[i] or t[j] cost:swapCost
        # i: s[i] t[i] cost: crossCost

        count = Counter(x + y for x, y in zip(s, t))

        # s: 0 0 1 1 1
        # t: 1 1 0 0 0
        # a = 1 / b = 4
        # (1 + 4) / 2 = 2

        a = count["01"]
        b = count["10"]
        if a > b:
            a, b = b, a

        # case1: flip cost small
        cost1 = (a + b) * flipCost
        # case2: swap cost small
        cost2 = a * swapCost + (b - a) * flipCost
        # case3: cross small, then swap final flip
        avg, rem = divmod(a + b, 2)
        cost3 = (avg - a) * crossCost + avg * swapCost + rem * flipCost

        return min(cost1, cost2, cost3)
