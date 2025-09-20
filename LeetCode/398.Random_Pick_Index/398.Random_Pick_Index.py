#!/usr/bin/env python3


class Solution:

    def __init__(self, nums: List[int]):
        # dic key:num, val:index array
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        if target in self.dic:
            return random.choice(self.dic[target])
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
