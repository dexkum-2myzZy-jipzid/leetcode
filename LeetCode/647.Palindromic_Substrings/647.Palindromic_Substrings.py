#!/usr/bin/env python3


class Solution:
    def countSubstrings(self, s: str) -> int:
        # central expanding

        n = len(s)

        def helper(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l, r = l - 1, r + 1
            return cnt

        res = 0
        for i in range(n):
            res += helper(i, i)
            if i + 1 < n:
                res += helper(i, i + 1)

        return res
