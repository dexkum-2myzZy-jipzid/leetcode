#!/usr/bin/env python3


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n = n // 10

        digits = digits[::-1]

        # 1. Find the first decreasing element from the right
        m = len(digits)
        i = m - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # not next permutation
        if i < 0:
            return -1

        # 2. Find the smallest digit on the right of i that is larger than digits[i]
        j = m - 1
        while digits[j] <= digits[i]:
            j -= 1

        # 3. swap
        digits[j], digits[i] = digits[i], digits[j]

        # 4. Reverse the subarray from i + 1 to end
        digits[i + 1 :] = reversed(digits[i + 1 :])

        res = 0
        for j in range(m):
            res = res * 10 + digits[j]

        return res if res <= 2**31 - 1 else -1
