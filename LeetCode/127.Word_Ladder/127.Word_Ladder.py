#!/usr/bin/env python3

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0
