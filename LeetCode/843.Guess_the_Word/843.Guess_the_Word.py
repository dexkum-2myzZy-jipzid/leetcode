#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, words: list[str], master: "Master") -> None:

        def match(a: str, b: str) -> int:
            return sum(aa == bb for aa, bb in zip(a, b))

        cands = set(words)

        while cands:
            word = cands.pop()
            m = master.guess(word)
            if m == 6:
                return word

            words = [w for w in cands if match(w, word) == m]
            cands = set(words)
