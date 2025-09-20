#!/usr/bin/env python3


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return (" ").join(reversed(arr))
