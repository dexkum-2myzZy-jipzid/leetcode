#!/usr/bin/env python3


# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali = ""
        for char in s.lower():
            if char.isalnum():
                pali += char
        return pali[:] == pali[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s => lowercase, remove non-alph char
        s = ("").join([c for c in s if c.isalnum()]).lower()
        return s == s[::-1]
