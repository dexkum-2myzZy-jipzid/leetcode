#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):

            new_word = word[:i] + word[i + 1 :]

            counter = Counter(new_word)

            if len(set(counter.values())) == 1:
                return True

        return False
