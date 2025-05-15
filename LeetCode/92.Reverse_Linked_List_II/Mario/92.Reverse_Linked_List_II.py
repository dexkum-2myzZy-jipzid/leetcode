#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # edge case
        if left == right:
            return head

        # hit the left
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = None, dummy
        index = 0

        while index < left:
            pre = cur
            cur = cur.next
            index += 1

        # print(pre.val)
        # print(cur.val)

        # reverse [left right]
        tmp, reverse = None, None
        left_node = cur  # set it to connect (right:]
        while index <= right and cur:
            tmp = cur
            cur = cur.next
            tmp.next = reverse
            reverse = tmp
            index += 1

        pre.next = reverse
        left_node.next = cur

        return dummy.next
