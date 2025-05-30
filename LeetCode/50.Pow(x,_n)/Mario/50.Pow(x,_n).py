#!/usr/bin/env python3


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pos_pow(x, n):
            # print(f"n:{n}")
            if n == 0:
                return 1.0
            half = pos_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / pos_pow(x, -n)
        else:
            return pos_pow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
            # print(f"x:{x}")
        return res
