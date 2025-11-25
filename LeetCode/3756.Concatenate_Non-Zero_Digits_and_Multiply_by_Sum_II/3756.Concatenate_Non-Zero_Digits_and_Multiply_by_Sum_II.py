#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:

        MOD = 10**9 + 7
        x, ans = 0, 0

        state = [(x, ans)]
        non_zero_s = []

        for i, ch in enumerate(s):
            if ch.isdigit():
                if ch != "0":
                    x += 1
                    non_zero_s.append(ord(ch) - ord("0"))
                    ans += int(ch)
            state.append((x, ans))

        m = len(non_zero_s)
        pref = [0] * (m + 1)  # pref[i] = non_zero_s[:i] 组成的数的值
        pow10 = [1] * (m + 1)  # pow10[i] = 10^i % MOD
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            pref[i] = (pref[i - 1] * 10 + non_zero_s[i - 1]) % MOD

        # print(state)
        # [('', 0), ('1', 1), ('1', 1), ('12', 3),
        #  ('12', 3), ('123', 6), ('123', 6),
        #  ('123', 6), ('1234', 10)]

        res = []

        for l, r in queries:
            (l_x, l_ans), (r_x, r_ans) = state[l], state[r + 1]

            # print(left, right)
            # ('', 0) ('1234', 10)
            # ('1', 1) ('12', 3)
            # ('12', 3) ('123', 6)

            ans = r_ans - l_ans
            length = r_x - l_x
            if length == 0:
                seg_val = 0
            else:
                seg_val = (pref[r_x] - pref[l_x] * pow10[length]) % MOD

            res.append(seg_val * ans % MOD)

        return res
