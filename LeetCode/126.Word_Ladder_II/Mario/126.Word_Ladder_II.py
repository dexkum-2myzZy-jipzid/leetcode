#!/usr/bin/env python3
from typing import List
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        m, n = len(beginWord), len(wordList)
        word_list = set(wordList)

        # edge case
        if endWord not in word_list:
            return []

        # wildcard bucket, e.g. h*t -> {hot, hit}
        buckets = defaultdict(set)
        for w in word_list:
            for i in range(m):
                buckets[w[:i] + "*" + w[i + 1 :]].add(w)

        q = deque([beginWord])
        vis = set()
        vis.add(beginWord)
        parent = defaultdict(list)

        # bfs first, get parent map
        found = False
        while q and not found:

            size = len(q)
            level_vis = set()

            for _ in range(size):
                cur = q.popleft()

                # find neigbhood wich differs by single letter
                for i in range(m):
                    key = cur[:i] + "*" + cur[i + 1 :]
                    for w in buckets[key]:
                        if w in vis:
                            continue

                        # using level_vis, to keep track of parent relationship
                        parent[w].append(cur)
                        if w == endWord:
                            found = True

                        if w not in level_vis:
                            level_vis.add(w)
                            q.append(w)

            vis.update(level_vis)

        # print(parent)

        res = []

        # backtrack, get result
        def backtrack(cur_word, path):
            if cur_word == beginWord:
                res.append(path[::-1])
                return

            for child in parent[cur_word]:
                backtrack(child, path + [child])

        backtrack(endWord, [endWord])

        return res
