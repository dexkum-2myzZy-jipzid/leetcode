#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # pick nums[i] and get its points, delete nums[i-1] & nums[i+1]
        # return max num of points

        # 1. counter nums, num: count : {2: 2, 3:3, 4:1}
        # 2. sort counter.keys keys = [2, 3, 4]
        # 3. using dp, dp[i] represent max points we can get in keys[:i]
        # cur_key, cur_key-1 in count,
        #     dp[i] = max(cur_key * count[cur_key] + dp[i-2], dp[i-1])

        count = Counter(nums)

        keys = sorted(count.keys())
        n = len(keys)

        dp = [0] * (n + 1)

        # init dp
        dp[1] = keys[0] * count[keys[0]]

        for i in range(2, n + 1):
            cur = keys[i - 1]
            points = cur * count[cur]
            if cur - 1 in count:
                dp[i] = max(points + dp[i - 2], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + points

        return dp[n]
