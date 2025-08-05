#!/usr/bin/env python3


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # valid:
        # "" / AB / (A)
        # one move: insert parenthesis

        left, right = 0, 0
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                left += 1
            elif c == ")":
                if left:
                    left -= 1
                else:
                    right += 1

        return left + right
