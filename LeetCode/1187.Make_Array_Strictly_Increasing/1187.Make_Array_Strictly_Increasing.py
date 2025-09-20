#!/usr/bin/env python3


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n = len(arr1)

        dp = {-1: 0}

        for num in arr1:
            next_dp = {}
            for prev, step in list(dp.items()):
                # no need swap
                if num > prev:
                    if num not in next_dp or next_dp[num] > step:
                        next_dp[num] = step

                # swap the num in arr1 with num in arr2
                # find smallest bigger num in arr2 than prev
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    swap_num = arr2[idx]
                    if swap_num not in next_dp or next_dp[swap_num] > step + 1:
                        next_dp[swap_num] = step + 1

            if not next_dp:
                return -1
            dp = next_dp

        return min(dp.values())
