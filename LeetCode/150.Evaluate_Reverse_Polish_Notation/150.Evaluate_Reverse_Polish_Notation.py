#!/usr/bin/env python3


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in set(["+", "-", "*", "/"]):
                last = stack.pop()
                if t == "+":
                    stack[-1] += last
                elif t == "-":
                    stack[-1] -= last
                elif t == "*":
                    stack[-1] *= last
                elif t == "/":
                    a = stack[-1]
                    stack[-1] = int(a / last)
            else:
                stack.append(int(t))

        return stack[-1]
