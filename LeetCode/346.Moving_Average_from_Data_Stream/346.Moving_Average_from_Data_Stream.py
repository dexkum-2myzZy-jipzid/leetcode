#!/usr/bin/env python3


class MovingAverage:

    def __init__(self, size: int):
        self.q = deque([])
        self.n = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.n:
            remove = self.q.popleft()
            self.sum -= remove

        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
