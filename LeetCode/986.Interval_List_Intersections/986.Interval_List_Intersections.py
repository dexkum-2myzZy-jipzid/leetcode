#!/usr/bin/env python3


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        # queue, store
        # comparet first element of list
        # a = [x, y] b = [u, v]
        # 1. y < u: pop a
        # 2. x > u: pop b
        # 3 intersection: max(x, u), min(y, v), keep end bigget interval, pop end small one

        first, second = deque(firstList), deque(secondList)
        res = []

        while first and second:
            x, y = first[0]
            a, b = second[0]

            # first is total left of second
            if y < a:
                first.popleft()
            elif b < x:  # second is total left of first
                second.popleft()
            else:
                l, r = max(x, a), min(y, b)
                res.append([l, r])
                if y > b:
                    second.popleft()
                elif y < b:
                    first.popleft()
                else:
                    first.popleft()
                    second.popleft()

        return res
