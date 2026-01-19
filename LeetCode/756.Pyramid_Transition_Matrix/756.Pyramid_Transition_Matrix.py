#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import cache
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # pre-process allowed
        allowed_dic = defaultdict(list)
        for e in allowed:
            allowed_dic[e[:2]].append(e[2])

        @cache
        def dfs(current_row, next_row, start):
            if len(current_row) == 1:
                return True

            if len(current_row) - 1 == start:
                return dfs(next_row, "", 0)

            key = current_row[start : start + 2]
            for nei in allowed_dic[key]:
                if dfs(current_row, next_row + nei, start + 1):
                    return True

            return False

        return dfs(bottom, "", 0)
