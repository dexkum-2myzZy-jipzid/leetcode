#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # prev, curr
        # one pass this linked list,
        # while curr.val == val, so prev.next = curr

        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr:
                curr = curr.next

        return dummy.next
