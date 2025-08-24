#!/usr/bin/env python3
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        # 1 or more groups
        # k distincts e
        # 1 e 1 group

        n = len(nums)
        if n % k != 0:
            return False

        group_size = n // k

        count = Counter(nums)
        max_cnt = max(count.values())
        # print(max_cnt)
        if group_size < max_cnt:
            return False

        return True
