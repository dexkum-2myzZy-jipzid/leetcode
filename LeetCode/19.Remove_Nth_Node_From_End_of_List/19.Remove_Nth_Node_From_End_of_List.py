#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer,
        dummy = ListNode(-1)
        dummy.next = head
        count = 0

        def reverse(pre):
            nonlocal count
            tmp = None
            cur = pre.next
            while cur:
                count += 1
                nxt = cur.next
                cur.next = tmp
                tmp = cur
                cur = nxt
            pre.next = tmp

        reverse(dummy)

        # no need to remove node
        if count < n:
            reverse(dummy)
            return head

        # remove nth node
        pre, cur = dummy, dummy.next
        count = 1

        while count <= n:
            if count == n:
                pre.next = cur.next
            else:
                cur = cur.next
                pre = pre.next
            count += 1

        reverse(dummy)

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n + 1):
            if not fast:  # this means n > the number of list nodes
                return head
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
