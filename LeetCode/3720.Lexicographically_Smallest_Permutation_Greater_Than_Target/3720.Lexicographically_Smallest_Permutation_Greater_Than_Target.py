#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # len(s) = len(target) = n, lowercase
        # sort: s > target

        def to_array(s: str) -> list[int]:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord("a")] += 1
            return cnt

        scnt, tcnt = to_array(s), to_array(target)

        res = []
        for i, c in enumerate(target):
            j = ord(c) - ord("a")
            if scnt[j] > 0:
                res.append(c)
                scnt[j] -= 1
                continue

            # find smallest greater than j index
            found = False
            for k in range(j + 1, 26):
                if scnt[k] > 0:
                    res.append(chr(ord("a") + k))
                    scnt[k] -= 1
                    found = True
                    break

            if found:
                for k in range(26):
                    if scnt[k] > 0:
                        ch = chr(ord("a") + k)
                        res.append(ch * scnt[k])
                return "".join(res)
            break
        else:
            pass

        while res:
            last = res.pop()
            li = ord(last) - ord("a")
            scnt[li] += 1

            for nxt in range(li + 1, 26):
                if scnt[nxt] > 0:
                    scnt[nxt] -= 1
                    res.append(chr(ord("a") + nxt))

                    for k in range(26):
                        if scnt[k] > 0:
                            ch = chr(ord("a") + k)
                            res.append(ch * scnt[k])
                    return "".join(res)

        return ""
