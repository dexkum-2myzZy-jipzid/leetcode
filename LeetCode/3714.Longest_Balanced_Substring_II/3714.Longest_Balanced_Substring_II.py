#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestBalanced(self, s: str) -> int:
        # s only contain a, b, c
        # sliding window x

        # only work for exist 3
        a = b = c = 0
        # for 3 char
        seen = {(0,0):-1}
        ab = {(0,0):-1}
        ac = {(0,0):-1}
        bc = {(0,0):-1}
        res = 0

        run_len = 0
        prev = None

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            key = (a-b, a-c)
            if key in seen:
                res = max(res, i-seen[key])
            else:
                seen[key] = i

            abk = (a-b, c)
            if abk in ab:
                res = max(res, i-ab[abk])
            else:
                ab[abk] = i

            ack = (a-c, b)
            if ack in ac:
                res = max(res, i-ac[ack])
            else:
                ac[ack] = i

            bck = (b-c, a)
            if bck in bc:
                res = max(res, i-bc[bck])
            else:
                bc[bck] = i

            if ch == prev:
                run_len += 1
            else:
                run_len = 1
                prev = ch
            res = max(res, run_len)

        return res
        