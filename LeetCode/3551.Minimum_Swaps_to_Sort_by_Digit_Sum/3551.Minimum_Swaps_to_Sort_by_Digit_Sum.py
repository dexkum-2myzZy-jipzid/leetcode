#!/usr/bin/env python3


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = [(sum(map(int, str(num))), num, i) for i, num in enumerate(nums)]
        # print(arr)
        arr.sort()

        idx_map = {e[2]: i for i, e in enumerate(arr)}
        # print(idx_map)

        n = len(arr)
        visited = [False] * n
        res = 0

        for i in range(n):
            if visited[i] or idx_map[i] == i:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = idx_map[j]
                cycle_len += 1

            res += cycle_len - 1

        return res
