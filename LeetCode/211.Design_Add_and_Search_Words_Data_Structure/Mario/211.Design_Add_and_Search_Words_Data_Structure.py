#!/usr/bin/env python3


class TrieNode:

    def __init__(self):
        self.children = {}  # key:str, val: TrieNode
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self._helper(word, self.root)

    def _helper(self, word, node0):
        node = node0
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
            elif c == ".":
                if len(node.children.keys()) == 0:
                    return False
                for key in node.children:
                    part = word[i + 1 :]
                    if self._helper(key + part, node):
                        return True
                return False
            else:
                return False

        return node.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
