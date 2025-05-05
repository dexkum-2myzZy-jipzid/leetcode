#!/usr/bin/env python3


class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = defaultdict(int)  # key: val, value: count
        self.timestamp = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        freq = self.count[val]
        self.timestamp += 1
        heapq.heappush(self.stack, (-freq, -self.timestamp, val))

    def pop(self) -> int:
        freq, index, val = heapq.heappop(self.stack)
        self.count[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


# using self.group {freq: list}, pop element from self.group[self.max_freq].pop()
class FreqStack:

    def __init__(self):
        self.group = defaultdict(list)  # freq:list
        self.max_freq = 0
        self.count = defaultdict(int)  # val:freq

    def push(self, val: int) -> None:
        f = self.count[val] + 1
        self.count[val] = f

        if f > self.max_freq:
            self.max_freq = f

        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()

        self.count[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
