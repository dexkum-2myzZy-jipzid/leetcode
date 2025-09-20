#!/usr/bin/env python3


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for e in path.split("/"):
            if e == "..":
                if stack:
                    stack.pop()
            elif e == "." or e == "":
                continue
            else:
                stack.append(e)

        return "/" + ("/").join(stack)
