#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for val in range(p * p, n, p):
                    is_prime[val] = False

        return sum(is_prime)
