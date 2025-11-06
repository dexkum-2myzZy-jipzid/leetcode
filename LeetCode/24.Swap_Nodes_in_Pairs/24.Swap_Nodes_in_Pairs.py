#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev => first => second

        # => prev => second => first
        # => prev = first / first = first.next / second = first.next.next

        # edge case
        # 0 / 1 node
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        first, second = head, head.next

        while first and second:
            prev.next = second
            nxt = second.next  # first node of next pair
            second.next = first
            first.next = nxt
            if nxt is None:
                break
            else:
                prev = first
                first, second = nxt, nxt.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev => first => second

        # => prev => second => first
        # => prev = first / first = first.next / second = first.next.next

        # edge case
        # 0 / 1 node
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)

        second.next = first

        return second
