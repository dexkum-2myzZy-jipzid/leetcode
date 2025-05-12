#!/usr/bin/env python3


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # build map char in s can map to char in s
        s_to_t, t_to_s = {}, {}
        for a, b in zip(s, t):
            if a not in s_to_t and b not in t_to_s:
                s_to_t[a] = b
                t_to_s[b] = a
            elif a in s_to_t and b in t_to_s:
                if s_to_t[a] == b and t_to_s[b] == a:
                    continue
                else:
                    return False
            else:
                return False

        return True
