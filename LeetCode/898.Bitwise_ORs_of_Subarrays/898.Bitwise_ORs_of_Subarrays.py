#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:

        # end with i-1 element
        prev = set()
        # result
        res = set()

        for i, num in enumerate(arr):

            cur = set([num])
            for p in prev:
                cur.add(p | num)

            res.update(cur)
            prev = cur

        return len(res)
