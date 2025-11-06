#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1,2,3,4,5]

        # 1 => 3 => 5

        # 4 => 2 => tail = None => reverse

        # only 0 or 1 node
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        count = 1
        prev, curr = dummy, head
        dummy2 = ListNode(-2)
        odd = dummy2

        while curr:
            if count % 2 == 1:
                curr = curr.next
                prev = prev.next
            else:
                nxt = curr.next
                curr.next = None
                odd.next = curr
                odd = curr
                prev.next = nxt
                curr = nxt
            count += 1

        prev.next = dummy2.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1,2,3,4,5]

        # odd: 1

        # even: 2

        # only 0 or 1 node
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
