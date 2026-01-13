#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def residuePrefixes(self, s: str) -> int:
        # lower case
        res = 0
        counter = Counter()
        for i, ch in enumerate(s):
            counter[ch] += 1
            if len(counter.keys()) == (i + 1) % 3:
                res += 1

        return res
