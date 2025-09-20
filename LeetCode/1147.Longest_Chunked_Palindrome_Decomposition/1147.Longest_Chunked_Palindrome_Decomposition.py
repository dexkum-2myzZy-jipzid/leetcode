#!/usr/bin/env python3


class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        for i in range(1, (n // 2) + 1):
            if text[:i] == text[-i:]:
                return self.longestDecomposition(text[i : n - i]) + 2
        return 1 if len(text) > 0 else 0
