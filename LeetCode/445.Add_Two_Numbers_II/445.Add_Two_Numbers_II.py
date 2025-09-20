#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def reverse(l):
            tail = None
            cur = l
            while cur:
                tmp = cur.next
                cur.next = tail
                tail = cur
                cur = tmp
            return tail

        l1 = reverse(l1)
        l2 = reverse(l2)

        node1, node2 = l1, l2
        carry = 0
        dummy = ListNode(-1, l1)
        cur = dummy
        while node1 or node2 or carry:
            tmp = carry
            if node1:
                tmp += node1.val
                node1 = node1.next

            if node2:
                tmp += node2.val
                node2 = node2.next

            carry = tmp // 10
            tmp %= 10
            if not cur.next:
                cur.next = ListNode(0)
            cur = cur.next
            cur.val = tmp

        return reverse(dummy.next)
