#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Logger:

    # t "hello"
    # t+5 "hello" filter,
    # t+11, "hello", still print

    # dict key:"message", value: time (true one)
    # in dict, i will check time, if current_time >= time + 10
    # print, also update time in dict
    # if not int dict, print, dict store message and time

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = timestamp
            return True
        else:
            if timestamp >= (self.dict[message] + 10):
                self.dict[message] = timestamp
                return True
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# using set and deque
class Logger:

    # self.deque = [] && self.seen = set()
    # self.deque (time, message)
    # self.deque first element,
    # timestamp >= first_element_time + 10
    # pop element, also, remove message from seen
    # if timestamp < first_element_time + 10:
    # if message in seen, it will return false,

    def __init__(self):
        self.queue = deque()
        self.seen = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # maintain this queue window, only contains message in [current_time-10, current_time]
        while self.queue and self.seen and (self.queue[0][0] + 10) <= timestamp:
            _, first_message = self.queue.popleft()
            self.seen.remove(first_message)

        if message in self.seen:
            return False
        else:
            self.queue.append((timestamp, message))
            self.seen.add(message)
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
