#!/usr/bin/env python3


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # wiggle sequence
        # dp[i][0] means include ith nums, the longest wiggle seq(positive)
        # dp[i][1] means include ith nums, the longest wiggle seq(negative)

        # dp[i][0] [0, i-1] max(dp[j][1]+1, dp[i][0])
        # dp[i][1] [0, i-1] max(dp[j][0]+1, dp[i][1])

        n = len(nums)

        # if n == 1:
        #     return 1

        up, down = 1, 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

            # print(f"pre:{nums[i-1]}\tcur:{nums[i]}")
            # print(f"up:{up}, down:{down}\n")

        return max(up, down)
