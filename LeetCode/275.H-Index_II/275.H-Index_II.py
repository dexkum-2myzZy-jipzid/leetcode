#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # at least h papers cited at least h times
        # citations = [0,1,3,5,6]
        # [0, 1, 3, 2, 1]

        n = len(citations)

        left, right = 0, n - 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            # update res
            papers = n - mid
            c = citations[mid]

            h_index = min(papers, c)
            res = max(res, h_index)

            # if c >= papers, keep looking for left side, find bigger papers,
            # so can make h_index bigger
            if c >= papers:
                right = mid - 1
            else:
                left = mid + 1

        return res
