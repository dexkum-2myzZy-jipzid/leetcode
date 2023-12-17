#!/usr/bin/env python3

pal = []
base = 1
while base <= 10000:
    for i in range(base, base*10):
        x = i
        t = i//10
        while t:
            x = x*10 + t % 10
            t //= 10
        pal.append(x)
    if base <= 1000:
        for i in range(base, base*10):
            x = t = i
            while t:
                x = x*10 + t % 10
                t //= 10
            pal.append(x)

    base *= 10
pal.append(10**9+1)


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def cost(i):
            target = pal[i]
            return sum(abs(x-target) for x in nums)

        i = bisect_left(pal, nums[(n-1)//2])

        if pal[i] <= nums[n//2]:
            return cost(i)

        return min(cost(i-1), cost(i))
