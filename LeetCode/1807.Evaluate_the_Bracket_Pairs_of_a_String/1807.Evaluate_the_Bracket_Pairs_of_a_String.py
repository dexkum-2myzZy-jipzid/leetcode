#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # 1. convert knowledge into map {key:value}
        # 2. for loop s,encouter "(",")", replace it

        dic = defaultdict(str)
        for k, v in knowledge:
            dic[k] = v

        in_bracket = False
        word = ""
        res = []
        for i, ch in enumerate(s):
            if ch == "(":
                in_bracket = True
            elif ch == ")":
                in_bracket = False
                val = dic[word] if word in dic else "?"
                res.append(val)
                word = ""
            elif in_bracket:
                word += ch
            else:
                res.append(ch)

        return "".join(res)
