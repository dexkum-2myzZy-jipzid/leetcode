#!/usr/bin/env python3


class Solution:
    def maximumSwap(self, num: int) -> int:
        # convert num to str, sort str array in reverse way
        str1 = list(str(num))
        str1.sort(reverse=True)

        str2 = str(num)
        res = []
        # find swap num, the big one
        # 7632 & 2736 -> 7 / 2
        swap = []  #
        for c1, c2 in zip(str1, str2):
            res.append(c1)
            # first time two digit not the same, then store it and break the iterate
            if c1 != c2:
                swap.append(c1)
                swap.append(c2)
                break

        swapIndex = -1
        # find the same last element in the left part
        for i in range(len(str2) - 1, len(res) - 1, -1):
            if str2[i] == res[-1]:
                swapIndex = i
                break

        for i in range(len(res), len(str2)):
            if i == swapIndex:
                res.append(swap[1])
            else:
                res.append(str2[i])

        return int(("").join(res))


class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(str(num))
        n = len(lst)

        last_occurrence = [-1] * 10
        for i, c in enumerate(lst):
            last_occurrence[ord(c) - ord("0")] = i

        for i, c in enumerate(lst):
            if c == "9":
                continue
            else:
                # find last occurrence of element which is bigger than c
                j = ord(c) - ord("0")
                for k in range(9, j, -1):
                    if last_occurrence[k] > i:
                        lst[i], lst[last_occurrence[k]] = f"{k}", c
                        return int(("").join(lst))

        return num
