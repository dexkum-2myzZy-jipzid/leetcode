#!/usr/bin/env python3


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if stack and c in dic and dic[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
