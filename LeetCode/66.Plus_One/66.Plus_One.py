#!/usr/bin/env python3


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            digits[i] = val % 10
            carry = val // 10

            if carry == 0:
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits
