#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# heap
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap store element (val, ListNode)

        heap = []
        dummy = ListNode(-1)
        node = dummy

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        if not heap:
            return None

        while heap:
            (val, i, list_node) = heapq.heappop(heap)

            node.next = list_node
            node = node.next

            if list_node.next:
                nxt = list_node.next
                heapq.heappush(heap, (nxt.val, i, nxt))

        return dummy.next


# divide and conquer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self._merge_lists(lists, 0, len(lists) - 1)

    def _merge_lists(self, lists, left, right):
        if left == right:
            return lists[left]
        # divide
        mid = (left + right) // 2
        left_node = self._merge_lists(lists, left, mid)
        right_node = self._merge_lists(lists, mid + 1, right)
        # conquer
        return self._merge_node(left_node, right_node)

    def _merge_node(self, p, q):
        dummy = ListNode(-1)
        node = dummy

        while p and q:
            if p.val < q.val:
                node.next = p
                p = p.next
            else:
                node.next = q
                q = q.next
            node = node.next

        node.next = p if p else q
        return dummy.next
