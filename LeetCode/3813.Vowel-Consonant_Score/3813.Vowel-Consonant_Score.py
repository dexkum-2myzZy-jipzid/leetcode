#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0
        for ch in s:
            if ch in "aeiou":
                v += 1
            elif ch.isdigit() or ch == " ":
                continue
            else:
                c += 1

        return floor(v / c) if c > 0 else 0
