#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestPrime(self, n: int) -> int:
        # prime num <= n

        # get array hold prime start from 2

        def get_primes(n: int) -> list[bool]:
            if n < 2:
                return []

            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for x in range(p * p, n + 1, p):
                        is_prime[x] = False
                p += 1

            return is_prime

        is_prime = get_primes(n)
        primes = [i for i, x in enumerate(is_prime) if x]
        primes_set = set(primes)

        res = 0
        if (not is_prime) or (not primes):
            return res

        # prefix_sum = []

        prefix = []
        for p in primes:
            if not prefix:
                prefix.append(p)
            else:
                prefix.append(prefix[-1] + p)

            last = prefix[-1]

            if last <= n and last in primes_set:
                res = last

        return res
