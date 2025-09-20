#!/usr/bin/env python3

from math import inf
from collections import defaultdict


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        # balanced: max_freq * (unique_chars) == lenght of substring

        n = len(s)
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dic = defaultdict(int)
            max_freq = 0
            for j in range(i - 1, -1, -1):
                dic[s[j]] += 1
                max_freq = max(max_freq, dic[s[j]])
                if max_freq * len(dic) == (i - j):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n]
