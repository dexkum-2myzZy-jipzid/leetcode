#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestBalanced(self, s: str) -> int:
        # balanced: all char freq is same
        n = len(s)
        res = 1
        for i in range(n):
            count = Counter()
            for j in range(i, n):
                count[s[j]] += 1
                lst = list(count.values())
                if j-i+1 > res and len(set(lst)) == 1:
                    res = j-i+1
        return res