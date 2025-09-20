#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count total number of nodes
        cnt = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            cnt += 1

        # Reverse k nodes starting from pre.next
        def rev(pre, cur):
            tail = cur
            prev = None
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            pre.next = prev  # Connect previous part to reversed head
            tail.next = cur  # Connect reversed tail to next part
            return tail, cur  # New pre and cur for next group

        # Dummy node to simplify head operations
        dum = ListNode(-1)
        dum.next = head
        pre, cur = dum, head

        # Reverse in groups of k
        for _ in range(cnt // k):
            pre, cur = rev(pre, cur)

        return dum.next
