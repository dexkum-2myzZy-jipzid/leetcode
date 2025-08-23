#!/usr/bin/env python3


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # break this weights into days segments, the sum of this segnment < res
        # get mini res
        n = len(weights)

        def check(x):
            cnt, seg = 1, 0
            for w in weights:
                if seg + w > x:
                    seg = 0
                    cnt += 1
                seg += w
            return cnt <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
