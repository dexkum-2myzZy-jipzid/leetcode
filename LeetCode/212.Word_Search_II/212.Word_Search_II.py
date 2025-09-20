#!/usr/bin/env python3


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie
        # current issue, how to handle so many path
        # 1. build trie by words
        # 2. dfs, search trie, if not, return

        m, n = len(board), len(board[0])
        root = TrieNode()

        def insert(word):
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word

        for w in words:
            insert(w)

        res = set()

        def dfs(i, j, node, cnt):
            ch = board[i][j]
            if ch not in node.children:
                return

            nxt = node.children[ch]
            if nxt.word:
                res.add(nxt.word)
                node.word = None

            if cnt > 10:
                return

            board[i][j] = "#"
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, nxt, cnt + 1)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, 0)

        return list(res)
