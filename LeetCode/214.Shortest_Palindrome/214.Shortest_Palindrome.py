#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        n = len(s)
        if n <= 1:
            return s

        rev = s[::-1]
        t = s + "#" + rev

        # 构建前缀函数（KMP）
        pi = [0] * len(t)
        for i in range(1, len(t)):
            j = pi[i - 1]
            while j > 0 and t[i] != t[j]:
                j = pi[j - 1]
            if t[i] == t[j]:
                j += 1
            pi[i] = j

        L = pi[-1]  # s 的最长回文前缀长度
        # 需要前置的部分 = s[L:] 的逆序 = rev[:n - L]
        return rev[: n - L] + s
