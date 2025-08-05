#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # lowercase letter
        stack = []

        for i, c in enumerate(s):

            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
