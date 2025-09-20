#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        # non-decreasing order
        # After the insertion, the circular list should remain sorted.

        # head is null, create a new single circular list
        insert = Node(insertVal)
        if not head:
            insert.next = insert
            return insert

        cur = head
        while True:
            # 1 [2] 3
            if cur.val <= insertVal <= cur.next.val:
                break
            # [1] 2 3 or 2 3 [4] cur is biggest, cur.next is smallest
            if cur.val > cur.next.val:
                if cur.val < insertVal or insertVal < cur.next.val:
                    break

            cur = cur.next
            # finished one pass
            if cur == head:
                break

        insert.next = cur.next
        cur.next = insert

        return head
