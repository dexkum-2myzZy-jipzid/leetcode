#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dfs(l: int, r: int, k: int) -> int:
            # 空区间
            if l > r:
                return 0

            # 步骤1：把右端与右侧“同色尾巴”合并（吸并）
            # 让 boxes[r] 连续段尽可能长，用 k 表示额外并到右侧的数量
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # 步骤2：直接打掉右端连续块（包含 k 个并入的同色）
            ans = dfs(l, r - 1, 0) + (k + 1) * (k + 1)

            # 步骤3：寻找与 boxes[r] 同色的位置 i，把中间清空后合并再打
            color = boxes[r]
            for i in range(l, r):
                if boxes[i] == color:
                    # 先清空 i 与 r 之间的 [i+1..r-1]
                    # 再把 boxes[i] 与右端一起作为更长的尾巴
                    ans = max(ans, dfs(l, i, k + 1) + dfs(i + 1, r - 1, 0))

            return ans

        return dfs(0, n - 1, 0)
