#!/usr/bin/env python3


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # test case 1:
        # at least 3 papers >= 3
        # test case 2:
        # no: at least 2 papers >= 2
        # yes: at least 1 papers >= 1
        # test case 3:
        # at least 1 papers >= 100
        # test case 4:
        # at least 1 papers >= 1

        citations.sort()
        n = len(citations)
        h = 0

        for i in range(n - 1, -1, -1):
            papers = n - i
            c = citations[i]

            if c >= papers:
                h = papers
            else:
                break

        return h
