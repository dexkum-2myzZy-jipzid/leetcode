#!/usr/bin/env python3


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n, m = len(s), len(words)

        # abcde => {a;[0], b:[1], c:[2], d:[3], e:[4]}
        # ace = 024

        dic = defaultdict(list)  # 26 letters
        for i, c in enumerate(s):
            dic[c].append(i)

        # print(dic)
        res = 0
        for w in words:
            if len(w) > n:
                continue
            else:
                pre = None
                is_sub = True
                for i, c in enumerate(w):
                    if c not in dic:
                        is_sub = False
                        break
                    else:
                        if not pre:
                            pre = dic[c][0]
                        else:
                            arr = dic[c]
                            idx = bisect.bisect_right(arr, pre)
                            # find idx bigger than pre
                            if idx == len(arr):
                                is_sub = False
                                break
                            else:
                                pre = arr[idx]
                if is_sub:
                    # print(w)
                    res += 1

        return res


# fewer code
from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 建立字典：字符 -> 索引列表
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)

        res = 0
        for w in words:
            pre = -1  # 初始化上一个字符的位置
            for c in w:
                if c not in dic:
                    break
                idx_list = dic[c]
                # 用 bisect 查找第一个大于 pre 的下标
                idx = bisect.bisect_right(idx_list, pre)
                if idx == len(idx_list):
                    break
                pre = idx_list[idx]
            else:
                res += 1  # 没有 break，说明是子序列
        return res
