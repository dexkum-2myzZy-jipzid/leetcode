#!/usr/bin/env python3


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        # sum of distance
        # collide, move opposite dir
        # [-3, -2, -1, 0, 1, 2]
        #      A.      B     C # RLL
        # 1       B/A    C
        # 2.   B       C/A
        # 3. B      C      A

        MOD = 10**9 + 7

        n = len(nums)
        pos = []
        for num, di in zip(nums, s):
            if di == "R":
                num += d
            elif di == "L":
                num -= d

            pos.append(num)

        pos.sort()
        res = 0
        for i in range(n):
            # for ith pos,
            # i times pos - others
            # (n-1-i) tims, others - pos
            contribution = pos[i] * (i - (n - 1 - i))
            res = (res + contribution) % MOD

        return res
