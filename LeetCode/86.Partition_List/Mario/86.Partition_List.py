#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dum1, dum2 = ListNode(-1), ListNode(-1)
        less, greater = dum1, dum2

        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next

        greater.next = None
        less.next = dum2.next

        return dum1.next
