#!/usr/bin/env python3


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        count.sort()
        return sum(count[:-k])
