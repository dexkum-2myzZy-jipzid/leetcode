#!/usr/bin/env python3


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # ops: sum(2 num) = k, remove them
        # max ops

        counter = Counter(nums)
        res = 0

        for num in list(counter.keys()):
            pair = k - num
            if pair not in counter:
                continue
            if pair == num:
                pairs = counter[num] // 2
                res += pairs
                counter[num] -= pairs * 2
            else:
                pairs = min(counter[num], counter[pair])
                res += pairs
                counter[num] -= pairs
                counter[pair] -= pairs

        return res
