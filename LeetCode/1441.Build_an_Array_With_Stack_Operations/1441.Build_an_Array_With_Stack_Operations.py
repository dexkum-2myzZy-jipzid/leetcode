#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        # simulate the whole process
        idx = 0
        res = []
        for num in range(1, n + 1):
            if idx >= len(target):
                break
            current = target[idx]
            res.append("Push")
            if current != num:
                res.append("Pop")
            else:
                idx += 1

        return res
