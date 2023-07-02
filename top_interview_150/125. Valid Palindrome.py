#!/usr/bin/env python3

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali = ""
        for char in s.lower():
            if char.isalnum():
                pali += char
        return pali[:] == pali[::-1]
