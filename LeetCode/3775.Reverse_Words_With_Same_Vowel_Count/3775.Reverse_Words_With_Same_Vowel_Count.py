#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        vowels = set(["a", "e", "i", "o", "u"])

        def get_vowel_count(s: str) -> int:
            res = 0
            for ch in s:
                if ch in vowels:
                    res += 1
            return res

        if arr == 0:
            return s

        count = get_vowel_count(arr[0])

        res = [arr[0]]
        for i in range(1, len(arr)):
            cur = arr[i]
            if get_vowel_count(cur) == count:
                res.append(cur[::-1])
            else:
                res.append(cur)

        return " ".join(res)
