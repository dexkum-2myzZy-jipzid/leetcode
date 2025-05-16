#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-101)
        dummy.next = head

        # pre, cur = dummy, head
        # compare cur and next nodes, if they are the same, store duplicate val, the cur -> next, next -> next.next
        # if cur_val > duplicate val, pre connect cur

        pre, cur = dummy, head
        dup = -101
        while cur:
            if cur.next and cur.val == cur.next.val:
                dup = cur.val
            elif cur.val > dup:
                pre.next = cur
                pre = cur
            elif not cur.next:  # cur is last node, but it still duplicate node
                pre.next = cur.next
            cur = cur.next

        return dummy.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-101)
        dummy.next = head

        # pre = dummy, cur = head
        # if cur.val == next.val, skip this part

        pre, cur = dummy, head
        while cur:
            dup = False
            while cur.next and cur.val == cur.next.val:
                dup = True
                cur = cur.next

            if dup:
                pre.next = cur.next
            else:
                pre.next = cur
                pre = cur

            cur = cur.next

        return dummy.next
