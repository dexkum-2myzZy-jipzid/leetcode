#!/usr/bin/env python3


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # diff dp
        # dp = {0:0} means diff = 0,  left length  = 0

        # name two side, left, right
        # for each rod
        # 1. add left, diff + rod
        # 2. add right: diff - rod
        # 3. not add:

        n = len(rods)
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()
            for diff, left_height in dp.items():
                # 1. add left, diff + rod
                right_height = left_height - diff
                new_dp[diff + rod] = max(new_dp.get(diff + rod, 0), left_height + rod)

                # 2. add right, abs(diff - rod)
                new_diff = diff - rod
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), left_height)

            dp = new_dp

        return dp[0]
