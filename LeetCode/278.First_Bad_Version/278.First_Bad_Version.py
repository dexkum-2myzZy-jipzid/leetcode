#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):  # bad version
                left = mid + 1
            else:
                right = mid

        return left


class Solution2:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):  # bad version
                left = mid + 1
            else:
                right = mid

        return left
