#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        squares.sort(key=lambda x: x[1])

        total = 0.0
        left, right = inf, -inf
        for x, y, l in squares:
            total += l * l
            left = min(left, y)
            right = max(right, y + l)

        def get_area_blew_line(k: float) -> float:
            area = 0.0
            for _, y, l in squares:
                # square above k line
                if y >= k:
                    break
                elif y + l <= k:
                    # square total below k line
                    area += l * l
                else:
                    area += (k - y) * l

            return area

        while (right - left) > 0.00001:
            mid = (left + right) / 2
            if get_area_blew_line(mid) * 2 < total:
                left = mid
            else:
                right = mid
            # print(f"left:{left}\tright:{right}")

        return left
