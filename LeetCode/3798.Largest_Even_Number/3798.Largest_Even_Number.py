#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestEven(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            digit = int(s[i])
            if digit % 2 == 0:
                return s[: i + 1]

        return ""
