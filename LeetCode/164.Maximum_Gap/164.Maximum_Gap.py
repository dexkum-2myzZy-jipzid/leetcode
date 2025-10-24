#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf, -inf

class Solution:
    def maximumGap(self, nums: list[int]) -> int:

        # time complexity: O(n) / space complexity: O(n)

        # handle edge case first: the length of num <= 1, return 0

        # the main ideas is bucket, max diff is definitly between buckets, not in bucket

        # get min, max value from nums,  bucket_size = (max - min) / (n-1)

        # two array, one is min bucket hold min value of this bucket
        # max buckets hold max value of this bucket

        # put every num in nums into buckets, update min / max value in bucket

        # then compare cur buckets min with prev bucket max, this diff, if diff > global diff,

        # update global diff

        n = len(nums)
        if n < 2:
            return 0

        max_val, min_val = max(nums), min(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))  # (9 - 1) / 3 = 2
        bucket_count = (max_val - min_val) // bucket_size + 1  # (9-1) / 2 = 5

        max_bucket = [-inf] * bucket_count
        min_bucket = [inf] * bucket_count

        for num in nums:
            i = (num - min_val) // bucket_size
            max_bucket[i] = max(num, max_bucket[i])
            min_bucket[i] = min(num, min_bucket[i])

        res = 0
        prev_max = max_bucket[0]
        for i in range(1, bucket_count):
            cur_min, cur_max = min_bucket[i], max_bucket[i]
            if cur_min == inf:
                continue
            else:
                res = max(cur_min - prev_max, res)
                prev_max = cur_max

        return res
