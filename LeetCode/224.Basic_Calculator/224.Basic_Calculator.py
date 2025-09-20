#!/usr/bin/env python3


class Solution:
    def calculate(self, s: str) -> int:
        """
        stack = [] "3 + (3+2)", stack can store 3, so we can focous on (3+2)
        sign = 1 if char is "+" else -1
        num store current num, becase some nums has mutilply digits
        """

        stack = []
        sign = 1
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                stack.append(sign * num)
                sign = -1 if ch == "-" else 1
                num = 0
            elif ch == "(":
                stack.append(sign)
                stack.append("(")
                sign = 1
                num = 0
            elif ch == ")":
                res = sign * num
                while type(stack[-1]) != str:
                    res += stack.pop()
                stack.pop()  # pop "("
                last_sign = stack.pop()
                stack.append(last_sign * res)
                sign = 1
                num = 0

        stack.append(sign * num)

        return sum(stack)
