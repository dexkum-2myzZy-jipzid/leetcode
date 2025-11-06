#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        tail = None
        node = mid

        while node:
            nxt = node.next
            node.next = tail
            tail = node
            node = nxt

        # tail 4 => 3
        # head 1 => 2
        node = dummy
        p1, p2 = head, tail

        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next

            node.next = p1
            p1.next = p2
            node = p2

            p1 = p1_next
            p2 = p2_next

        if p1:
            node.next = p1

        return dummy.next
