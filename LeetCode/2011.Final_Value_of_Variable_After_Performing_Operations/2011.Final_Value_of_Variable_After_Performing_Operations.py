#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increment, decrement = 0, 0
        for op in operations:
            if op in ["X++", "++X"]:
                increment += 1
            elif op in ["--X", "X--"]:
                decrement += 1

        return increment - decrement
