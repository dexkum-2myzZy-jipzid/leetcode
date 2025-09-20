#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # 0-1
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        arr.reverse()

        res, i = 0, 0
        for j, val in enumerate(arr):
            res += val * (2**i)
            i += 1

        return res
