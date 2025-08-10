#!/usr/bin/env python3


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        # greedy order
        # active smallest limit[i] corrsponding value
        # for limit l, only can active l num of elements
        # sum(top l largest num) for every limit l group

        group = defaultdict(list)
        for v, l in zip(value, limit):
            group[l].append(v)

        res = 0
        for l, arr in group.items():
            arr.sort(reverse=True)
            res += sum(arr[:l])

        return res
