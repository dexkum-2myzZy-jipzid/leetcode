#!/usr/bin/env python3


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        # check length
        if len(words) != len(pattern):
            return False
        p_to_w, w_to_p = {}, {}
        for ch, w in zip(pattern, words):
            if ch not in p_to_w and w not in w_to_p:
                p_to_w[ch] = w
                w_to_p[w] = ch
            elif ch in p_to_w and w in w_to_p:
                if p_to_w[ch] == w and w_to_p[w] == ch:
                    continue
                else:
                    return False
            else:
                return False

        return True
