#!/usr/bin/env python3


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1. empty str, contains only lowercase
        # 2. AB
        # 3. A

        n = len(s)
        res = []
        stack = []  # store index of '('

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                res.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                    res.append(c)
                else:
                    res.append("")
            else:
                res.append(c)

        for i in stack:
            res[i] = ""

        return ("").join(res)
