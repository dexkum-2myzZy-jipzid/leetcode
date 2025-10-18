#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        n = len(words)
        # handle edge case
        if n == 0:
            return []

        def signature(w: str) -> tuple[int, ...]:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord("a")] += 1
            return tuple(cnt)

        res = [words[0]]
        sig = signature(words[0])
        i = 1

        while i < n:
            cur = words[i]
            cur_sig = signature(cur)
            # they are not anagrams
            if sig != cur_sig:
                sig = cur_sig
                res.append(cur)
            i += 1

        return res
