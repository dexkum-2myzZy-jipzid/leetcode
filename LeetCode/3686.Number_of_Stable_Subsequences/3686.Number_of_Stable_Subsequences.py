#!/usr/bin/env python3


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # subseq is table ==  not 3 consecutive elments
        # return num of stable subseq
        MOD = 10**9 + 7

        # end with odd, the max odd len is 1
        odd1 = odd2 = even1 = even2 = 0

        for num in nums:
            # odd
            o1, o2, e1, e2 = odd1, odd2, even1, even2
            if num & 1 == 1:
                odd1 = (o1 + e1 + e2 + 1) % MOD
                odd2 = (o2 + o1) % MOD
            else:
                even1 = (1 + odd1 + odd2 + even1) % MOD
                even2 = (even2 + e1) % MOD

        return (odd1 + odd2 + even1 + even2) % MOD
