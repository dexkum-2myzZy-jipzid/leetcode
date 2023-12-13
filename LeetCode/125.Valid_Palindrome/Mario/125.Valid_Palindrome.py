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
        s = ''.join([v for v in s if v.isalnum()]).lower()
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True 
