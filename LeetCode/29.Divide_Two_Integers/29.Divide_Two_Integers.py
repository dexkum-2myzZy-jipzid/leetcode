#!/usr/bin/env python3


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 10 - 3*2 = 4
        # 4 - 3 * 1 = 1
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        neg = (dividend < 0) != (divisor < 0)
        dvd, dvr = abs(dividend), abs(divisor)

        res = 0

        while dvd >= dvr:
            tmp = 0
            while dvd >= (dvr << (tmp + 1)):
                tmp += 1

            res += 1 << tmp
            dvd -= dvr << tmp

        return -res if neg else res
