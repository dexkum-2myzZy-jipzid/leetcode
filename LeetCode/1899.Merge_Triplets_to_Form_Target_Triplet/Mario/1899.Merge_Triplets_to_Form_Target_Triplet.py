#!/usr/bin/env python3


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # elements in triplets <= target[i]
        # check every position of element can reach target val

        res = [False, False, False]

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    if t[i] == target[i]:
                        res[i] = True
                if all(res):
                    return True

        return all(res)
