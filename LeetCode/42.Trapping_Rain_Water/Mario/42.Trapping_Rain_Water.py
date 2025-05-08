#!/usr/bin/env python3


class Solution:
    def trap(self, height: List[int]) -> int:
        # using monotonic stack, store decreasing array,
        # when meet a number is bigger than last element of stack,
        # it means that format a place can trap water

        stack = []
        n = len(height)
        res = 0  # how much water trap
        for i, h in enumerate(height):

            while stack and height[stack[-1]] < h:
                bottom = height[stack.pop()]
                if not stack:
                    break
                left = stack[-1]
                minH = min(height[left], h) - bottom
                res += minH * (i - left - 1)

            stack.append(i)

        return res
