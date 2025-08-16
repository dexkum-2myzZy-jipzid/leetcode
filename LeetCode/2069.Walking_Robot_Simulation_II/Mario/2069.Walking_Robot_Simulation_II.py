#!/usr/bin/env python3

from typing import List


class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.w, self.h = width, height
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.idx = 0
        self.pos = (0, 0)
        self.perimeter = (self.w + self.h) * 2 - 4

    def step(self, num: int) -> None:

        num %= self.perimeter

        if num == 0 and self.pos == (0, 0) and self.idx == 0:
            self.idx = 3
            return

        while num:
            x, y = self.pos

            if self.idx == 0:  # face east
                moves = min(self.w - x - 1, num)
                self.pos = (x + moves, y)
            elif self.idx == 1:  # north
                moves = min(self.h - 1 - y, num)
                self.pos = (x, y + moves)
            elif self.idx == 2:  # west
                moves = min(x, num)
                self.pos = (x - moves, y)
            else:  # south
                moves = min(y, num)
                self.pos = (x, y - moves)

            num -= moves
            if num > 0:
                self.idx = (self.idx + 1) % 4

    def getPos(self) -> List[int]:
        return list(self.pos)

    def getDir(self) -> str:
        return Robot.TO_DIR[self.idx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()


class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.w, self.h = width, height
        self.pos = 0

    def step(self, num: int) -> None:
        # self.pos range = [1,(w+h-2)*2]
        self.pos = (self.pos + num - 1) % ((self.w + self.h - 2) * 2) + 1

    def getPos(self) -> List[int]:
        w, h = self.w, self.h
        if self.pos < w:
            return [self.pos, 0]
        elif self.pos < w + h - 1:
            return [w - 1, self.pos - w + 1]
        elif self.pos < w * 2 + h - 2:
            return [2 * w + h - 3 - self.pos, h - 1]
        else:
            return [0, (w + h - 2) * 2 - self.pos]

    def getDir(self) -> str:
        if self.pos < self.w:
            return "East"
        elif self.pos < self.w + self.h - 1:
            return "North"
        elif self.pos < self.w * 2 + self.h - 2:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
