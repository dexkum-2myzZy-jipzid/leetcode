#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # divide and conquer
        if not head or not head.next:
            return head
        # break down into two linked lists
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        l = self.sortList(dummy.next)
        r = self.sortList(right)

        # merge
        return self.merge(l, r)

    def merge(self, l, r):
        if not l and not r:
            return None

        dummy = ListNode(-1)
        p = dummy
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next

        if l:
            p.next = l
        if r:
            p.next = r

        return dummy.next
