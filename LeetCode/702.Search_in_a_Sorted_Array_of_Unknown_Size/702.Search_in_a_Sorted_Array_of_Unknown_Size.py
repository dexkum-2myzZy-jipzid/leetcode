#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        left, right = 0, 1

        # expand right boundary, also locate target in [left, right] range
        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
