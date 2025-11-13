#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        curr = (startTime, endTime)
        idx = bisect.bisect_left(self.events, curr)  # start <= startTime (current)
        #!!! bisect_right pass all test case

        n = len(self.events)
        # check left neighbor
        if idx - 1 >= 0:
            if self.events[idx - 1][1] > curr[0]:
                return False

        # check right neighbor
        if idx < n:
            if curr[1] > self.events[idx][0]:
                return False

        self.events.insert(idx, curr)
        return True
