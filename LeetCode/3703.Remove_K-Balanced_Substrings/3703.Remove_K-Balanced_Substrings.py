#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = [] # ["(", cnt]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            if len(stack) >= 2:
                last, prev = stack[-1], stack[-2]
                if last[0] == ")" and last[1] == k:
                    if prev[0] == "(" and prev[1] >= k:
                        # pair, pop k * ()
                        stack.pop()
                        if prev[1] == k:
                            stack.pop()
                        else:
                            stack[-1][1] -= k 

        return "".join([ch*cnt for ch, cnt in stack])