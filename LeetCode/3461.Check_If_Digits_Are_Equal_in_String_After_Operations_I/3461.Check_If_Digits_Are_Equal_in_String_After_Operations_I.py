#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def hasSameDigits(self, s: str) -> bool:

        def dfs(digits: list[int]) -> bool:
            if len(digits) == 2:
                return True if digits[0] == digits[1] else False

            res = []
            for i in range(1, len(digits)):
                digit = (digits[i - 1] + digits[i]) % 10
                res.append(digit)

            return dfs(res)

        digits = [int(ch) for ch in s]

        return dfs(digits)


class Solution2:
    def hasSameDigits(self, s: str) -> bool:

        digits = [int(ch) for ch in s]
        while len(digits) > 2:
            n = len(digits)
            for i in range(1, n):
                digits[i - 1] = (digits[i - 1] + digits[i]) % 10
            digits.pop()

        return True if digits[0] == digits[1] else False
