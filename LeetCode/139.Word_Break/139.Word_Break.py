#!/usr/bin/env python3


# tc: O(n * m) / n = len(s), m = len(wordDict)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[n+1]
        # iterate word dict
        # for each word: dp[i] = dp[i-len(word)] if we can find s[i:i+len(word)] = curent word

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # "" is True

        for i in range(1, n + 1):
            for w in wordDict:
                left = i - len(w)
                if left >= 0 and dp[left]:
                    if s[left:i] == w:
                        dp[i] = True
                if dp[i]:
                    break

        # print(dp)

        return dp[n]


# tc: O(n * n) / n = len(s)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[n+1]
        # iterate word dict
        # for each word: dp[i] = dp[i-len(word)] if we can find s[i:i+len(word)] = curent word

        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # "" is True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
