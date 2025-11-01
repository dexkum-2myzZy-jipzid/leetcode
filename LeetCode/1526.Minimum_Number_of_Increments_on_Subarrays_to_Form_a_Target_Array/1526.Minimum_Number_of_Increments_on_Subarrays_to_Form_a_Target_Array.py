#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minNumberOperations(self, target: list[int]) -> int:

        # initial -> min num of operations -> target

        # target = [1,2,3,2,1] -> initial
        # 0, 1, 2, 3, 4
        # [1, 1, 1, -1, -1]
        # [3,-2,-0, 1]
        # [3,-2,4,-1,-2]

        # sum(positive integer in difference array)

        diff_array = []

        for i, t in enumerate(target):
            if i == 0:
                diff_array.append(t)
            else:
                diff_array.append(t - target[i - 1])

        return sum([x for x in diff_array if x > 0])
