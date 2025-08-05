#!/usr/bin/env python3


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2

        # every fruits should be even
        for k, cnt in total.items():
            if cnt % 2 == 1:
                return -1

        stack1, stack2 = [], []  # [element, swap count]
        for k in total:
            diff = count1[k] - count2[k]
            if diff > 0:
                stack1.append([k, diff // 2])
            elif diff < 0:
                stack2.append([k, -diff // 2])

        # print(f"stack1:{stack1}\nstack2:{stack2}")

        min_swap = min(total) * 2
        stack1.sort()
        stack2.sort(reverse=True)

        res = 0
        while stack1:
            f1, c1 = stack1.pop()
            f2, c2 = stack2.pop()
            cost = min(f1, f2, min_swap)
            res += cost * min(c1, c2)
            if c1 > c2:
                stack1.append([f1, c1 - c2])
            elif c1 < c2:
                stack2.append([f2, c2 - c1])

        return res
