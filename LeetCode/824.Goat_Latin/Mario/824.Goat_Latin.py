#!/usr/bin/env python3


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr = sentence.split(" ")
        res = []
        for i, w in enumerate(arr):
            tmp = ""
            if w[0] in "aeiouAEIOU":
                tmp = w + "ma" + (i + 1) * "a"
            else:
                tmp = w[1:] + w[:1] + "ma" + (i + 1) * "a"
            res.append(tmp)

        return (" ").join(res)
