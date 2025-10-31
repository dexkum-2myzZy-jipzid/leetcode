#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return 0
            # k: 最小使 (2^k - 1) >= t 的 k
            k = t.bit_length()
            full = (1 << k) - 1
            if full == t:
                return k  # 直接 A^k 命中

            # 方案1：超射后回头
            ans = k + 1 + dp(full - t)  # A*k + R + dp(差额)

            # 方案2：欠射，先到 (2^(k-1)-1)，再 R，探回 m 步，再 R，补剩余
            # m ∈ [0, k-2]
            half = (1 << (k - 1)) - 1
            for m in range(k - 1):  # m = 0..k-2
                back = (1 << m) - 1
                rem = t - (half - back)  # 剩余要前进的距离
                cand = (k - 1) + 1 + m + 1 + dp(rem)  # (k-1)A + R + mA + R + dp(rem)
                if cand < ans:
                    ans = cand
            return ans

        return dp(target)
