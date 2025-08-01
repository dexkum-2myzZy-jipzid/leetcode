#!/usr/bin/env python3


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # counter(s)
        # based on order to permute

        count = Counter(s)

        res = ""
        for i, c in enumerate(order):
            if c in count:
                res += c * count[c]
            del count[c]

        for k, v in count.items():
            res += k * v

        return res
