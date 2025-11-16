#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        # count(a) == count(b), remove substring
        # return min length

        count = Counter(s)
        return abs(count["a"] - count["b"])
