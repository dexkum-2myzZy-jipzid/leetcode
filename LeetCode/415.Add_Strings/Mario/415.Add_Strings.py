#!/usr/bin/env python3


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry > 0:
            digit = carry

            if i >= 0:
                digit += int(num1[i])
                i -= 1

            if j >= 0:
                digit += int(num2[j])
                j -= 1

            carry = digit // 10
            digit %= 10

            res.append(str(digit))

        return "".join(res[::-1])
