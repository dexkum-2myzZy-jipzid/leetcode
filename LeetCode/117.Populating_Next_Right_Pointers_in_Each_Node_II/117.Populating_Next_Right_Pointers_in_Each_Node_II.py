#!/usr/bin/env python3


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        cur = root
        while cur:
            dummy = Node(-1)
            child = dummy
            while cur:
                if cur.left:
                    child.next = cur.left
                    child = child.next
                if cur.right:
                    child.next = cur.right
                    child = child.next
                cur = cur.next
            cur = dummy.next
        return root
