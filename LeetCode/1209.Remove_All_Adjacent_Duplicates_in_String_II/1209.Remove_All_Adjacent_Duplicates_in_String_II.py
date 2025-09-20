#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, times]

        for i, c in enumerate(s):

            if not stack or (stack and stack[-1][0] != c):
                stack.append([c, 1])
            elif stack and stack[-1][0] == c:
                if stack[-1][1] + 1 < k:
                    stack[-1][1] += 1
                else:
                    stack.pop()

        return "".join([c * t for c, t in stack])
