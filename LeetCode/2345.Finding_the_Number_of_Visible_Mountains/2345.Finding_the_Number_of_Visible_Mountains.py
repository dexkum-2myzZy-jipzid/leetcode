#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from math import inf


class Solution:
    def visibleMountains(self, peaks: list[list[int]]) -> int:
        mountains = []
        # A:[left, right] B:[left, right]
        # if leftA <= leftB and rightB <= rightA;
        # means: b lie within A
        for x, y in peaks:
            mountains.append((y - x, y + x))

        counts = Counter(mountains)

        unique_mounts = sorted(counts.keys(), key=lambda x: (-x[0], -x[1]))

        res = 0
        prev_right = -inf

        for left, right in unique_mounts:
            # lie within
            if right <= prev_right:
                continue
            else:
                prev_right = right
                if counts[(left, right)] == 1:
                    res += 1

        return res
