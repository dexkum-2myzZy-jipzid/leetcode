#!/usr/bin/env python3


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # abc 0: ""  1: "abc" / 2: "abcabc"

        # times = len(b) // len(a)

        def substring(na, b):
            k = len(b)
            for i in range(len(na)):
                if na[i : i + k] == b:
                    # print(na)
                    return True
            return False

        t = (len(b) + len(a) - 1) // len(a)

        for i in range(t, t + 3):
            if substring(i * a, b):
                return i

        return -1


# 1. b = a + na + a
# 2. b in na to check b is substring
