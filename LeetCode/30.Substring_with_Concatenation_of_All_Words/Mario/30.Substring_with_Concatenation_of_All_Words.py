#!/usr/bin/env python3


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, k = len(s), len(words), len(words[0])
        counter = Counter(words)

        res = []
        for i in range(k):
            # sliding window
            l = r = i
            cur = Counter()
            count = 0  # increment the word count in cur window

            while r + k <= n:
                w = s[r : r + k]
                r += k

                if w in counter:
                    cur[w] += 1
                    if cur[w] <= counter[w]:
                        count += 1

                    while cur[w] > counter[w]:
                        l_word = s[l : l + k]
                        cur[l_word] -= 1
                        if cur[l_word] < counter[l_word]:
                            count -= 1
                        l += k

                    if count == m:
                        res.append(l)
                        cur[s[l : l + k]] -= 1
                        count -= 1
                        l += k
                else:
                    cur.clear()
                    l = r
                    count = 0

        return res
