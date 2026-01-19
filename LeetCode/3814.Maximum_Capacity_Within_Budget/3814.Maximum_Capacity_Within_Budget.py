#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left


class Solution:
    def maxCapacity(self, costs: list[int], capacity: list[int], budget: int) -> int:
        n = len(costs)
        group = [(cost, cap) for cost, cap in zip(costs, capacity)]
        group.sort()

        c = [i for i, _ in group]
        ca = [j for _, j in group]

        prefix = [0] * n
        for i in range(n):
            prefix[i] = ca[i] if i == 0 else max(prefix[i - 1], ca[i])

        res = 0
        for i in range(n):
            if c[i] < budget:
                res = max(res, ca[i])

            remain = budget - c[i]
            if remain <= 0:
                continue

            index = bisect_left(c, remain, 0, i)
            if index - 1 >= 0:
                res = max(res, ca[i] + prefix[index - 1])

        return res
