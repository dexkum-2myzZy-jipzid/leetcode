#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        # binary search mini speed
        # for loop mid speed, chech it can arrvied the office
        # if not, left = mid + 1, if can, right = mid

        n = len(dist)

        if hour <= n - 1:
            return -1

        def can_reach(k: int) -> bool:
            res = 0.0
            for i in range(n - 1):
                res += (dist[i] + k - 1) // k

            res += dist[-1] / k
            return res <= hour

        left, right = 1, max(dist) * 100
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
