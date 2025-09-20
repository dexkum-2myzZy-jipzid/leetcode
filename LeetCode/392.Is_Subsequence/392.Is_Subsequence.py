#!/usr/bin/env python3

# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
