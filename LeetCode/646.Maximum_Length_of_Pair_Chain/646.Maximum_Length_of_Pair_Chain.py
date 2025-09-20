#!/usr/bin/env python3


# dp
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])

        n = len(pairs)

        # dp[i] pairs[:i] include i, max length

        dp = [1] * n

        for i in range(1, n):
            i_start = pairs[i][0]
            for j in range(i):
                if pairs[j][1] < i_start:
                    dp[i] = dp[j] + 1

        return max(dp)


# greedy
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy， sort paris by right

        pairs.sort(key=lambda x: x[1])

        count, end = 1, pairs[0][1]

        for i, [l, r] in enumerate(pairs):
            if l > end:
                end = r
                count += 1

        return count
