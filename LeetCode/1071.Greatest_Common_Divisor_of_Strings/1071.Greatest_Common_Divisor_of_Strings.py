#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # make sure str1 = k1 * t, str2 = k2 * t
        # if not, return ""

        if str1 + str2 != str2 + str1:
            return ""

        g = gcd(len(str1), len(str2))

        return str1[:g]
