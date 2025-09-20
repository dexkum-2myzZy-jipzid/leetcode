#!/usr/bin/env python3


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bolds = [False] * n

        for w in words:
            start = 0
            while True:
                i = s.find(w, start)
                if i == -1:
                    break
                # mark bold
                for j in range(i, i + len(w)):
                    bolds[j] = True
                start = i + 1

        # print(bolds)

        tmp = ""
        res = ""
        for i in range(n):
            if bolds[i]:
                tmp += s[i]
            else:
                if tmp:
                    res += "<b>" + tmp + "</b>"
                    tmp = ""
                res += s[i]

        if tmp:
            res += "<b>" + tmp + "</b>"

        return res
