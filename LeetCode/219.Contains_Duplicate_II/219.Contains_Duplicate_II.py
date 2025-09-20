#!/usr/bin/env python3


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}  # num : index

        for i, n in enumerate(nums):
            if n in dic:
                if i - dic[n] <= k:
                    return True
            dic[n] = i

        return False
