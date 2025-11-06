#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse mid linked list
        tail = None
        node = mid
        while node:
            nxt = node.next
            node.next = tail
            tail = node
            node = nxt

        l1, l2 = head, tail
        while l1 and l2:
            if l1.val == l2.val:
                l1 = l1.next
                l2 = l2.next
            else:
                return False

        return True
