#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyCalendarThree:

    # sweep line

    def __init__(self):
        self.booked = []  # (start, +1), (end, -1)

    def book(self, startTime: int, endTime: int) -> int:
        self.booked.append((startTime, 1))
        self.booked.append((endTime, -1))

        self.booked.sort()

        max_room = current_room = 0

        for _, delta in self.booked:
            current_room += delta
            max_room = max(max_room, current_room)

        return max_room


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
