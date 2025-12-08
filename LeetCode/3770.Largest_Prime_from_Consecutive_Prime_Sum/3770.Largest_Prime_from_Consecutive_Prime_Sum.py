#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestPrime(self, n: int) -> int:

        # 1. get array contains all prime number
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        primes = [i for i in range(2, n + 1) if is_prime[i]]

        res = total = 0
        for p in primes:
            total += p
            if total > n:
                break

            if is_prime[total]:
                res = total

        return res
