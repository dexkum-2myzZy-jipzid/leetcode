#!/usr/bin/env python3


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]
        heap = []

        for i, p in enumerate(primes):
            heapq.heappush(heap, (p, i, 0))  # (value, prime index, dp index)

        while len(dp) < n:
            val, i, idx = heapq.heappop(heap)

            if dp[-1] != val:
                dp.append(val)

            next_idx = idx + 1
            next_val = primes[i] * dp[next_idx]
            heapq.heappush(heap, (next_val, i, next_idx))

        return dp[-1]
