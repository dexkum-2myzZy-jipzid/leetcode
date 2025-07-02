#!/usr/bin/env python3


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = Counter(s)
        in_stack = set()

        for ch in s:
            count[ch] -= 1

            if ch in in_stack:
                continue

            # greedy
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                top = stack.pop()
                in_stack.remove(top)

            stack.append(ch)
            in_stack.add(ch)

        return ("").join(stack)
