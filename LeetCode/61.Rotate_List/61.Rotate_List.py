#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the number of list node
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        if n == 0:
            return head

        k %= n

        if k == 0:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy

        for _ in range(k + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        cur = slow.next  # 4->5
        slow.next = None  # slow: 3

        new_dum = ListNode(-1)
        new_dum.next = cur

        while cur:
            if not cur.next:
                cur.next = dummy.next
                break
            cur = cur.next

        return new_dum.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the number of list node
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        if n == 0:
            return head

        k %= n

        if k == 0:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # Make the list circular
        fast.next = dummy.next
        new_head = slow.next
        slow.next = None

        return new_head
