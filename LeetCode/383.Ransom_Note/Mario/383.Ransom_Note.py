#!/usr/bin/env python3


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for c in ransomNote:
            if c in count and count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True
