#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:

        potions.sort()
        n = len(potions)
        res = []

        for spell in spells:
            # find index which potions[i] >= success / spell
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1

            count = n - left
            res.append(count)

        return res
