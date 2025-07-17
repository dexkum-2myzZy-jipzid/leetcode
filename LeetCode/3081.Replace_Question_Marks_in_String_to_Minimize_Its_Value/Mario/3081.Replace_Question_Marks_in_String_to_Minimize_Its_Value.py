#!/usr/bin/env python3


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # s[i] lowercase or "?"
        # cost[i] = freq before i
        # replace all occur "?"
        # min sum val

        heap = []

        counter = [0] * 26
        for i, c in enumerate(s):
            if c != "?":
                idx = ord(c) - ord("a")
                counter[idx] += 1

        # (freq, idx, c)
        for i, freq in enumerate(counter):
            c = chr(ord("a") + i)
            heapq.heappush(heap, [freq, i, c])

        # ? take 0 freq, then take min freq
        res = []
        arr = []
        for i, c in enumerate(s):
            if c == "?":
                freq, i, ch = heapq.heappop(heap)
                # print(freq, i, c)
                arr.append(ch)
                heapq.heappush(heap, [freq + 1, i, ch])
            res.append(c)

        j = 0
        arr.sort()
        for i in range(len(res)):
            if res[i] == "?":
                res[i] = arr[j]
                j += 1

        return ("").join(res)
