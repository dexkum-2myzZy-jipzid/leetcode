#!/usr/bin/env python3


class DetectSquares:

    def __init__(self):
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # print(self.cnt)
        x, y = point

        res = 0
        for (a, b), count in self.cnt.items():
            # rule itself
            if a == x and b == y:
                continue
            # if it's square, so side is the same
            if abs(a - x) == abs(b - y):
                p1 = (a, y)
                p2 = (x, b)
                if p1 in self.cnt and p2 in self.cnt:
                    res += self.cnt[p1] * self.cnt[p2] * count

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
