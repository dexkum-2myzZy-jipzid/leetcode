#!/usr/bin/env python3


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def helper(k):
            rem_set = set(removable[:k])
            i = j = 0
            while i < len(s) and j < len(p):
                if i in rem_set:
                    i += 1
                elif s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(p)

        left, right = 0, len(removable)
        res = 0
        while left <= right:
            mid = (left + right) >> 1
            if helper(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1

        return res
