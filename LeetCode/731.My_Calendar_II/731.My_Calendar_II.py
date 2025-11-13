#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyCalendarTwo:

    # no triple booking, [startTime, endTime)
    # sweep line check if max room >= 3
    # how to insert this room
    # events = [(time, delta)] start + 1, end - 1

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        tmp = self.events[:]
        tmp.append((startTime, 1))
        tmp.append((endTime, -1))

        tmp.sort()
        current_room = 0
        for _, delta in tmp:
            current_room += delta
            if current_room >= 3:
                return False

        self.events = tmp
        return True


class MyCalendarTwo2:

    def __init__(self):
        self.booked = []  # [start, end)
        self.overlap = []  #  [start, end)

    def book(self, startTime: int, endTime: int) -> bool:

        for start, end in self.overlap:
            if endTime <= start or end <= startTime:
                continue
            else:
                return False

        for start, end in self.booked:
            if endTime <= start or end <= startTime:
                continue
            else:
                self.overlap.append((max(start, startTime), min(end, endTime)))

        self.booked.append((startTime, endTime))
        return True
