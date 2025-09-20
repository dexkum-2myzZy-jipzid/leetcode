#!/usr/bin/env python3


class Solution:
    def resultingString(self, s: str) -> str:
        # len(s) >= 2

        def check_consecutive(a, b):
            pos1 = ord(a) - ord("a")
            pos2 = ord(b) - ord("a")

            return (pos1 - pos2) % 26 == 1 or (pos2 - pos1) % 26 == 1

        stack = []

        for i, ch in enumerate(s):

            if stack and check_consecutive(ch, stack[-1]):
                stack.pop()
            else:
                stack.append(ch)

        return ("").join(stack)
