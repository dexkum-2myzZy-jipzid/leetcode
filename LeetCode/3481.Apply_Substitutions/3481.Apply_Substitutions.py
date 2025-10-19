#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque, defaultdict


class Solution:
    def applySubstitutions(self, replacements: list[list[str]], text: str) -> str:
        q = deque([])

        graph = defaultdict(str)
        for k, v in replacements:
            if "%" in v:
                q.append(k)
            graph[k] = v

        def dfs(k: str) -> str:
            if k not in graph:
                return ""

            val = graph[k]
            if "%" not in val:
                return val

            vals = val.split("%")
            res = ""
            for v in vals:
                if v.islower():
                    res += v
                else:
                    ans = dfs(v)
                    graph[v] = ans
                    res += ans
            return res

        while q:
            k = q.popleft()
            graph[k] = dfs(k)

        arr = text.split("%")
        res = ""
        for e in arr:
            if e.isupper():
                res += graph[e]
            else:
                res += e

        return res
