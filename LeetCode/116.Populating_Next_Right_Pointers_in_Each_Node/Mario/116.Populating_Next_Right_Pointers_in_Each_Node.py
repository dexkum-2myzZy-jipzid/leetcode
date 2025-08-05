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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # edge case
        if not root:
            return root

        leftmost = root

        # if leftmost.left is null, means reach last layer of tree
        # out of this while loop
        while leftmost.left:
            head = leftmost
            # if head is null, means reach the end of current layer
            while head:
                # 1. head left connect right
                head.left.next = head.right
                # 2. head right connect next head left
                if head.next:
                    head.right.next = head.next.left
                head = head.next

            # move to next layer
            leftmost = leftmost.left

        return root
