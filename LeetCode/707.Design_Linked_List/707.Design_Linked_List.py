#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Optional


class Node:

    def __init__(
        self,
        val: int = -1,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        i = 0
        curr = self.head.next
        while i < self.size:
            if i == index:
                return curr.val
            else:
                i += 1
                curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        curr = Node(val, self.head, self.head.next)
        nxt = self.head.next

        self.head.next = curr
        nxt.prev = curr
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = Node(val, self.tail.prev, self.tail)
        prev = self.tail.prev

        prev.next = curr
        self.tail.prev = curr
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
            return

        i = 0
        curr = self.head.next

        while i < index and curr:
            curr = curr.next
            i += 1

        new_node = Node(val, curr.prev, curr)
        prev = curr.prev
        prev.next = new_node
        curr.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        i = 0
        curr = self.head.next

        while i < index and curr:
            i += 1
            curr = curr.next

        prev = curr.prev
        nxt = curr.next

        prev.next = nxt
        nxt.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
