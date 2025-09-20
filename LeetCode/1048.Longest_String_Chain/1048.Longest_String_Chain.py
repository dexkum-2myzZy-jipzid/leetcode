#!/usr/bin/env python3


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda x: len(x))
        # print(words)

        n = len(words)
        dp = [1] * n
        dic = defaultdict(int)  # key: word, value: index
        for i, w in enumerate(words):
            dic[w] = i

        for i, w in enumerate(words):
            for j in range(len(w)):
                tmp = w[:j] + w[j + 1 :]
                if tmp in dic:
                    k = dic[tmp]
                    dp[i] = max(dp[i], dp[k] + 1)

        return max(dp)
