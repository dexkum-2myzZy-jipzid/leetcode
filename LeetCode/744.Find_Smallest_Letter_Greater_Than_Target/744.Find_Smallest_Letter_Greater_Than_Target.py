#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        res = letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                res = letters[mid]
                right = mid - 1
            else:
                left = mid + 1

        return res
