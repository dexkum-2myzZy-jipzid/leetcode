#!/usr/bin/env python3


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # grid: n * n
        # rectangle no overlap

        # [1, 5], [0, 2], [3, 5], [0, 4]
        # [2, 4], [1], [4], [1, 2, 3]
        # [1, 2, 3, 4]

        # [0, 2], [2, 3], [2, 4],  [4, 5]
        # [0, 2], [2, 3], [2, 4], [4, 5]

        h_arr = [[r[0], r[2]] for r in rectangles]
        v_arr = [[r[1], r[3]] for r in rectangles]

        def helper(arr):
            arr.sort()
            cuts = 0
            last_end = arr[0][1]

            for i in range(1, len(arr)):
                start, end = arr[i]
                if last_end <= start:
                    cuts += 1
                last_end = max(last_end, end)

                if cuts >= 2:
                    return True
            return False

        # print(helper(h_arr))
        # print(helper(v_arr))

        return helper(h_arr) or helper(v_arr)
