#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        # monotonic stack
        # heights = [1,5,6,2]
        # stack = [0, 1, 2] hold index corrsponding value is non-decreasing

        # right = 3
        # last = 2, height = 6
        # left = stack[-1] = 1
        # width = right - left  - 1 # 3 - 1 - 1 = 1
        # max_area = 6

        heights = [0] + heights + [0]
        stack = []
        max_rect = 0

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                last = stack.pop()
                left = stack[-1]
                width = i - left - 1
                max_rect = max(max_rect, width * heights[last])

            stack.append(i)

        return max_rect
