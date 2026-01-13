#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def countPairs(self, words: list[str]) -> int:
        n, m = len(words), len(words[0])

        res = 0
        count = Counter()
        for word in words:
            base = ord(word[0])
            key = []
            for i in range(1, m):
                dist = (ord(word[i]) - base) % 26
                key.append(dist)
            key_tuple = tuple(key)
            res += count[key_tuple]
            count[key_tuple] += 1
        return res
