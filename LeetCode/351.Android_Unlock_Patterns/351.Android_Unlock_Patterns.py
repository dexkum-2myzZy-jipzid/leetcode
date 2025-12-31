#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        centers = set([(1, 3), (1, 7), (1, 9), (2, 8), (3, 9), (3, 7), (4, 6), (7, 9)])

        # mask means which num i used
        # prev: prev num i used
        # pos: current num i will use
        def dfs(mask, prev, pos) -> int:
            res = 0
            if pos >= m:
                res += 1

            if pos == n:
                return res

            for i in range(1, 10):
                # check it visited before or not
                if (mask >> (i - 1)) & 1:
                    continue
                # check if it in invalid pattern
                can_jump = True
                x, y = min(prev, i), max(prev, i)
                if (x, y) in centers:
                    current_center = (x + y) // 2
                    if not (mask & (1 << (current_center - 1))):
                        can_jump = False

                if can_jump:
                    res += dfs(mask | (1 << (i - 1)), i, pos + 1)

            return res

        return dfs(0, -1, 0)


class Solution2:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # 1. 预处理跳跃表
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8
        skip[1][7] = skip[7][1] = 4
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5

        seen = [False] * 10

        # curr: current value
        # remain: the count of remaing to jump
        def backtrack(curr: int, remain: int) -> int:
            if remain == 1:
                return 1

            seen[curr] = True
            res = 0
            for i in range(1, 10):
                # i node visited before
                # this jump need center, and center not visisted previous
                if (seen[i]) or (skip[curr][i] != 0 and not seen[skip[curr][i]]):
                    continue

                res += backtrack(i, remain - 1)

            seen[curr] = False
            return res

        res = 0
        for i in range(m, n + 1):
            res += backtrack(1, i) * 4
            res += backtrack(2, i) * 4
            res += backtrack(5, i)

        return res
