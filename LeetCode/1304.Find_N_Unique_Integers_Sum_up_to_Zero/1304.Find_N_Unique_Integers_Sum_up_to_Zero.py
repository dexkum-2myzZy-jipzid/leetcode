#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # 5, 5 /2 = 2, 1, 2,-1,- 2,
        half = n // 2
        res = []
        for i in range(1, half + 1):
            res.append(i)
            res.append(-i)

        if n % 2 == 1:
            res.append(0)
        return res
