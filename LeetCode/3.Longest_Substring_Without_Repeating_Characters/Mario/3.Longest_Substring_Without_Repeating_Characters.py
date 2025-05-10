#!/usr/bin/env python3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}  # key: char, value: index
        left = 0
        res = 0

        for right, char in enumerate(s):

            if char in dic and dic[char] >= left:
                left = dic[char] + 1

            dic[char] = right
            res = max(res, right - left + 1)

        return res
