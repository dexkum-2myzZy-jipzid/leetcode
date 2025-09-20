#!/usr/bin/env python3


class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0
        while n > 0:
            n //= 5
            # print(f"n:{n}")
            count += n

        return count
