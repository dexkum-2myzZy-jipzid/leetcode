#!/usr/bin/env python3

import random

MAX_LEVEL = 16


class SkipListNode:

    def __init__(self, val, level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * level


class Skiplist:

    def __init__(self):
        self.head = SkipListNode(-1)
        self.level = 0

    def random_level(self):
        level = 1
        while level < MAX_LEVEL and random.random() < 0.5:
            level += 1
        return level

    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]

        cur = cur.forward[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        lv = self.random_level()
        self.level = max(self.level, lv)
        new_node = SkipListNode(num, lv)
        for i in range(lv):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        # value is not exist
        if cur is None or cur.val != num:
            return False

        for i in range(self.level):
            if update[i].forward[i] != cur:
                break
            update[i].forward[i] = cur.forward[i]

        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
