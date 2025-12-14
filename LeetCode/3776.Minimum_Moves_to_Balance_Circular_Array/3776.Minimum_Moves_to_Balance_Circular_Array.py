#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minMoves(self, balance: list[int]) -> int:
        n = len(balance)

        if sum(balance) < 0:
            return -1
        elif min(balance) >= 0:
            return 0

        # left test case has exactly 1 negative element
        # find negative element index
        idx = -1
        for i, b in enumerate(balance):
            if b < 0:
                idx = i
                break

        need = -balance[idx]
        res = 0
        for d in range(1, n // 2 + 1):
            s = balance[idx - d] + balance[(idx + d) % n]
            if s >= need:
                res += need * d
                return res
            else:
                need -= s
                res += s * d

        return res
