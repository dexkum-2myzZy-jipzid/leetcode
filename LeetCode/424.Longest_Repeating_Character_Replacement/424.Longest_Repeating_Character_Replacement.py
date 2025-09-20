#!/usr/bin/env python3


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_freq = 0
        count = Counter()
        j = 0
        res = 0
        for i, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])

            while i - j + 1 > max_freq + k:
                count[s[j]] -= 1
                j += 1

            res = max(res, i - j + 1)

        return res
