#!/usr/bin/env python3


import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd, sum_even = 0, 0
        for i in range(1, 2 * n + 1):
            if i % 2 == 1:
                sum_odd += i
            else:
                sum_even += i

        return math.gcd(sum_odd, sum_even)
