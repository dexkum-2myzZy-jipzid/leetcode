#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:

        # brute force

        # heights = [10,6,8,5,11,9]
        # stack = [11, 5]
        # res = [0]
        # 8

        n = len(heights)
        res = [0] * n
        stack = [heights[-1]]

        for i in range(n - 2, -1, -1):
            see = 0
            while stack and stack[-1] < heights[i]:
                see += 1
                stack.pop()

            if stack:
                see += 1

            stack.append(heights[i])
            res[i] = see

        return res
