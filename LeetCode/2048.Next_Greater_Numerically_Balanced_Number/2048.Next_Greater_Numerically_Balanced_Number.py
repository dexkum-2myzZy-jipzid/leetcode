#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        # start n, n+1, s = str(n+1)

        # check s is balanced or not, if balanced, so return it, if not, continue increment n

        def is_balanced(s: str) -> bool:
            count = Counter(s)
            for k, v in count.items():
                if int(k) == v:
                    continue
                else:
                    return False
            return True

        while True:
            next_n = n + 1
            if is_balanced(str(next_n)):
                return next_n
            else:
                n = next_n

        return -1
