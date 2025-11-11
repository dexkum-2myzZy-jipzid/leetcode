#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class SnapshotArray:

    # self.snap_times = 0
    # self.snapArray = [[],[], []]

    # [[(0, 5), (1, 6)], [], []]
    # (snap_times, val)

    def __init__(self, length: int):
        self.snap_times = 0
        self.snap_array = [[(-1, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snap_array[index].append((self.snap_times, val))

    def snap(self) -> int:
        self.snap_times += 1
        return self.snap_times - 1

    def get(self, index: int, snap_id: int) -> int:
        array = self.snap_array[index]
        idx = bisect.bisect_right(array, (snap_id, 10**9)) - 1
        return array[idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
