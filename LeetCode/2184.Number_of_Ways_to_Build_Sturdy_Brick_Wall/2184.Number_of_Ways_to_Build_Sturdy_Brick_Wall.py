#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter
from functools import cache


class Solution:
    def buildWall(self, height: int, width: int, bricks: list[int]) -> int:

        MOD = 10**9 + 7

        # the count of combination bricks in one row
        # {mask: count}
        counter = Counter()

        @cache
        def get_all_mask(pos: int, mask: int):

            if pos == width:
                counter[mask] += 1
                return

            for b in bricks:
                nxt = pos + b
                if nxt > width:
                    continue

                new_mask = mask
                if nxt < width:
                    bit = nxt - 1
                    new_mask |= 1 << bit

                get_all_mask(nxt, new_mask)

        get_all_mask(0, 0)

        all_masks = list(counter.keys())

        @cache
        def dfs(h: int, prev_mask: int) -> int:

            if h == height:
                return 1

            total = 0
            for mask in all_masks:
                # adjacent rows in the wall should not join bricks at the same location
                if mask & prev_mask == 0:
                    count = dfs(h + 1, mask)
                    total = (total + count * counter[mask]) % MOD

            return total

        return dfs(0, 0)
