#!/usr/bin/env python3


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    # link list if use node, put node to the last the link list

    def __init__(self, capacity: int):
        self.n = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.dic = {}  # key:node
        self.head.next = self.tail
        self.tail.pre = self.head

    def _remove(self, node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    # add left most after head
    def _add(self, node):
        nxt = self.head.next
        node.next = nxt
        nxt.pre = node
        node.pre = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.dic:
            cur = self.dic[key]
            self._remove(cur)
            self._add(cur)
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            cur = self.dic[key]
            self._remove(cur)
            self._add(cur)
            cur.val = value
        else:
            if len(self.dic) == self.n:
                lru = self.tail.pre
                self._remove(lru)
                del self.dic[lru.key]
            cur = Node(key, value)
            self.dic[key] = cur
            self._add(cur)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
