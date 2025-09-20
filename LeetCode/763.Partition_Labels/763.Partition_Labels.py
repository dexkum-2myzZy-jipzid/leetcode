#!/usr/bin/env python3


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # dic: letter:[start, end]
        # res hold final answers list
        # i = 0, right = dic[s[0]][1]

        dic = {ch: i for i, ch in enumerate(s)}

        res = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(dic[ch], end)
            if i == end:
                res.append(end - start + 1)
                start = end + 1

        return res
