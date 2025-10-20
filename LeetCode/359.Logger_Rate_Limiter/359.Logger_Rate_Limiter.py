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
