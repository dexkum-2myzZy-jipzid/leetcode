#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import cache


class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)

        @cache
        def dfs(pos: int, tight: bool, started: bool) -> int:

            if pos == len(s):
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9
            res = 0

            for d in range(0, limit + 1):
                ntight = tight and (d == limit)

                if not started:
                    if d == 0:
                        res += dfs(pos + 1, ntight, False)
                    else:
                        res += dfs(pos + 1, ntight, True)
                else:
                    if d == 0:
                        continue
                    res += dfs(pos + 1, ntight, True)

            return res

        return dfs(0, True, False)
