#!/usr/bin/env python3


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # rank r n cars in r * n ** 2 m

        # sort ranks
        # left = ranks[0] * cars ** 2 right = ranks[-1] * cars ** 2

        n = len(ranks)

        def helper(time):
            cnt = 0
            for r in ranks:
                cnt += int(sqrt(time // r))
                if cnt >= cars:
                    return True
            return True if cnt >= cars else False

        left, right = 1, min(ranks) * (cars**2) + 1
        res = inf
        while left < right:
            mid = (left + right) >> 1
            if helper(mid):
                res = min(res, mid)
                right = mid
            else:
                left = mid + 1
        return res
