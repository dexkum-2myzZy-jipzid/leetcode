#!/usr/bin/env python3


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                # empty stack
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
