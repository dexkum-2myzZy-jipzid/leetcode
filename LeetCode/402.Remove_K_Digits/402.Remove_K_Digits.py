#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # monotonic stack
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # if k > 0, remove last k element
        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"
