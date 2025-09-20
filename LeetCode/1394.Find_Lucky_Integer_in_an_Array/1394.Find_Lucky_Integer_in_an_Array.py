#!/usr/bin/env python3


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for val in arr:
            dic[val] += 1

        res = -1
        for k in dic:
            if k == dic[k] and k > res:
                res = k

        return res
