#!/usr/bin/env python3


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            cur = carry

            if i >= 0:
                a_int = int(a[i])
                cur += a_int
                i -= 1

            if j >= 0:
                b_int = int(b[j])
                cur += b_int
                j -= 1

            carry = cur // 2
            res.append(str(cur % 2))

        return "".join(res[::-1])
