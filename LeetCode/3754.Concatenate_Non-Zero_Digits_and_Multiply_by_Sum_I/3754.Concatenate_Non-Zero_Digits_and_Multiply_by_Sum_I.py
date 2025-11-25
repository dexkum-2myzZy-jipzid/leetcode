#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        x, ans = 0, 0
        for ch in s:
            if ch.isdigit():
                cur = int(ch)
                if cur == 0:
                    continue
                x = x * 10 + cur
                ans += cur

        return x * ans
