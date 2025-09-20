#!/usr/bin/env python3


# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l,r  r >= l
        # l == r dp[l][r] = True
        # l == r-1 if s[l] == s[r] : dp[l][r] == True
        # dp[l][r] = (s[l] == s[r]) and dp[l+1][r-1]

        n = len(s)
        start, max_len = 0, 1

        # init dp
        dp = [[False] * n for _ in range(n)]

        # 'a' every character itself is pali / two characters
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if max_len < 2:
                    start, max_len = i, 2

        # iterate  l + 1 < r
        for length in range(3, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                print(f"l:{l}, r:{r}")
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    if length > max_len:
                        start, max_len = l, length

        return s[start : start + max_len]


# expand around center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l, r):
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1

        start, max_len = 0, 1

        for i in range(n):
            # odd
            l1, r1 = expand(i, i)
            if r1 - l1 + 1 > max_len:
                start, max_len = l1, r1 - l1 + 1

            # even
            if i + 1 < n:
                l2, r2 = expand(i, i + 1)
                if r2 - l2 + 1 > max_len:
                    start, max_len = l2, r2 - l2 + 1

        return s[start : start + max_len]
