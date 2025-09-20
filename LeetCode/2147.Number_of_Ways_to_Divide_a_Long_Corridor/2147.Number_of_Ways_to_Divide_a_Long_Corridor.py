#!/usr/bin/env python3


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # S seat / P plan
        # dividers [1, n-1]
        # exactly 2 seats + x plant

        MOD = 10**9 + 7

        n = len(corridor)

        prefix = [0] * (n + 1)
        for i, c in enumerate(corridor):
            prefix[i + 1] = prefix[i] + (1 if c == "S" else 0)

        seats = prefix[-1]
        # seats < 2 or sections is odd
        if seats < 1 or seats % 2 == 1:
            return 0

        res = 1
        cnt = 0
        start = 2
        for i in range(1, n + 1):
            cur = prefix[i]
            if cur == start:
                cnt += 1
            elif cur == (start + 1):
                res = (res * cnt) % MOD
                cnt = 0
                start += 2

        return res
