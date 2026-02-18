#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)

        # edge case
        if n < k:
            return 0

        counter = Counter(s)

        for ch, cnt in counter.items():
            if cnt < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))

        return len(s)
