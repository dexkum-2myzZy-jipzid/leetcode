#!/usr/bin/env python3

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 1. 建立 word -> index 的映射
        idx = {w: i for i, w in enumerate(words)}
        ans = []

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        # 2. 枚举每个单词及其所有切分点
        for i, w in enumerate(words):
            m = len(w)
            for k in range(m + 1):
                prefix, suffix = w[:k], w[k:]

                # 情况 A：prefix 是回文，后面接 rev(suffix)
                if is_palindrome(prefix):
                    j = idx.get(suffix[::-1])
                    if j is not None and j != i:
                        ans.append([j, i])

                # 情况 B：suffix 是回文，前面接 rev(prefix)
                # k < m 避免 suffix == "" 时重复
                if k < m and is_palindrome(suffix):
                    j = idx.get(prefix[::-1])
                    if j is not None and j != i:
                        ans.append([i, j])

        return ans


# Trie
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_word_idx = -1
        self.pali_suff = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # check if word is palindromePairs
        def is_pali(w):
            return w == w[::-1]

        # create trie
        root = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1]
            node = root
            for j, c in enumerate(word):
                if is_pali(word[j:]):
                    node.pali_suff.append(i)
                node = node.children[c]
            node.end_word_idx = i

        # search word in the trie and find palindrome pairs
        res = []
        for i, word in enumerate(words):
            node = root
            for j, c in enumerate(word):
                if node.end_word_idx != -1:
                    if is_pali(word[j:]):
                        res.append([i, node.end_word_idx])
                if c not in node.children:
                    break
                node = node.children[c]
            else:
                if node.end_word_idx not in [-1, i]:
                    res.append([i, node.end_word_idx])

                for j in node.pali_suff:
                    res.append([i, j])

        return res
