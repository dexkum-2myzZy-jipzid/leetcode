#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


class MyStack:

    def __init__(self):
        self.main = deque()
        self.supp = deque()

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while len(self.main) > 1:
            self.supp.append(self.main.popleft())

        last = self.main.popleft()
        self.main, self.supp = self.supp, self.main
        return last

    def top(self) -> int:
        while len(self.main) > 1:
            self.supp.append(self.main.popleft())

        last = self.main.popleft()
        self.supp.append(last)
        self.main, self.supp = self.supp, self.main
        return last

    def empty(self) -> bool:
        return not self.main and not self.supp


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# using one queue
class MyStack:

    # stack: first-in-last-out,
    # queue: first-in-first-out
    # push: if i push, i should put current element in
    # pop: popleft() [top, second....]

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
