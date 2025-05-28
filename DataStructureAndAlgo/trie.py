#!/usr/bin/env python3

from typing import Optional


class TrieNode:
    """Node in a Trie storing children and end-of-word flag."""

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """Trie supporting insert, search, and prefix queries."""

    def __init__(self):
        self.root = TrieNode()

    def _traverse(self, s: str) -> Optional[TrieNode]:
        """Traverse the trie according to string s; return last node or None."""
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return bool(node and node.is_end)

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word in the trie starts with the given prefix."""
        node = self._traverse(prefix)
        return node is not None
