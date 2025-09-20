#!/usr/bin/env python3

from math import inf
from collections import Counter


class Solution:
    def beautySum(self, s: str) -> int:
        # only sum len(str) >= 3

        # sliding window
        n = len(s)
        res = 0
        for start in range(n):
            max_freq, min_freq = 0, inf
            count = Counter()
            for i in range(start, n):
                count[s[i]] += 1
                if count[s[i]] > max_freq:
                    max_freq = count[s[i]]
                min_freq = min(count.values())

                # print(f"substr:{s[start:i+1]}\nmax:{max_freq}\tmin_freq:{min_freq}")
                if max_freq > min_freq:
                    res += max_freq - min_freq

        return res
