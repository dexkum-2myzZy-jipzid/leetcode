#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])
        times, vals = self.store[key]
        times.append(timestamp)
        vals.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        times, vals = self.store[key]
        idx = bisect.bisect_right(times, (timestamp)) - 1

        return "" if idx < 0 else vals[idx]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TimeMap2:

    # key:[timestamp]
    # timestamp: value

    def __init__(self):
        self.store = defaultdict(list)
        self.times = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # timestamp_prev <= timestamp
        if key not in self.store:
            return ""

        array = self.store[key]
        idx = bisect.bisect_right(array, timestamp) - 1
        if 0 <= idx < len(array):
            return self.times[array[idx]]
        return ""
