#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        n = len(words)
        res = []

        for i in range(n):
            top = words[i]
            for j in range(n):
                if i == j:
                    continue
                left = words[j]
                if top[0] == left[0]:
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        right = words[k]

                        if top[3] == right[0]:
                            for h in range(n):
                                if h == i or h == j or h == k:
                                    continue
                                bottom = words[h]
                                if bottom[0] == left[3] and bottom[3] == right[3]:
                                    res.append([top, left, right, bottom])

        res.sort()
        return res
