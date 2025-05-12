#!/usr/bin/env python3


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            res = 0
            while n > 0:
                val = n % 10
                res += val * val
                n //= 10
            return res

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_next(n)

        return True
