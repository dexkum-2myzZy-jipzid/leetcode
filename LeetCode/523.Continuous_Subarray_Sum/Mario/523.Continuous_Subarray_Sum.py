#!/usr/bin/env python3


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            if mod in prefix:
                if i - prefix[mod] >= 2:
                    return True
            else:
                prefix[mod] = i

        return False
