#!/usr/bin/env python3


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # a->s1, b->s2
        @cache
        def dfs(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                no_swap = dfs(a[:i], b[:i]) and dfs(a[i:], b[i:])
                if no_swap:
                    return True
                # s1[0:i] vs s2[n-i:n]
                swap = dfs(a[:i], b[n - i :]) and dfs(a[i:], b[: n - i])
                if swap:
                    return True
            return False

        return dfs(s1, s2)
