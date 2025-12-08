#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from typing import List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:

        n = len(damage)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + damage[i - 1]

        res = 0
        for i in range(n):

            need = prefix[i + 1] + requirement[i] - hp

            j = bisect.bisect_left(prefix, need, 0, i + 1)

            if j <= i:
                res += i - j + 1

        return res
