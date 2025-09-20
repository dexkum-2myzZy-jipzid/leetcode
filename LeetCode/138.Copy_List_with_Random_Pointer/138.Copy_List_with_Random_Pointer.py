#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        dic = {}  # old node to new node

        # copy all nodes
        cur = head
        while cur:
            new = Node(cur.val)
            dic[cur] = new
            cur = cur.next

        # set relationship
        cur = head
        while cur:
            new = dic[cur]
            if cur.next:
                new.next = dic[cur.next]

            if cur.random:
                new.random = dic[cur.random]

            cur = cur.next

        return dic[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # A -> A' -> B -> B'

        if not head:
            return None

        # copy new node then insert it
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # set random node
        cur = head
        while cur:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            cur = cur.next.next

        # decouple orign node and copy node
        cur = head
        copy_head = head.next
        copy = head.next
        while cur:
            nxt = cur.next.next
            if nxt:
                copy_nxt = nxt.next
                copy.next = copy_nxt
                copy = copy_nxt
            cur.next = nxt
            cur = nxt

        return copy_head
