#!/usr/bin/env python3


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # leftmost capcity >= qty of fruits
        # each basket one type
        # return num of fruits type unplaced

        n = len(fruits)
        res = 0
        for i, f in enumerate(fruits):
            found = False
            for j in range(n):
                if f <= baskets[j]:
                    baskets[j] = 0
                    found = True
                    break
            if not found:
                res += 1

        return res
