#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:

        # iterate s, get all i, the same to b, get all i and j
        # if abs(j-i) <= k, add i to result

        def helper(a: str) -> list[int]:
            n = len(s) - len(a)
            if n < 0:
                return []
            res = []
            for i in range(n + 1):
                if s[i : i + len(a)] == a:
                    res.append(i)
            return res

        a_array, b_array = helper(a), helper(b)

        res = []
        if not b_array:
            return res

        for i in a_array:
            idx = bisect.bisect_left(b_array, i)
            j = b_array[idx] if idx < len(b_array) else b_array[-1]

            if abs(j - i) <= k:
                res.append(i)
            elif idx - 1 >= 0:
                j = b_array[idx - 1]
                if abs(j - i) <= k:
                    res.append(i)

        return res
