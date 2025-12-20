#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:

        n = 0
        nums = []
        node = head
        while node:
            nums.append(node.val)
            n += 1
            node = node.next

        res = [0] * n
        stack = []

        for i, num in enumerate(nums):

            while stack and nums[stack[-1]] < num:
                last = stack.pop()
                res[last] = num

            stack.append(i)

        return res
