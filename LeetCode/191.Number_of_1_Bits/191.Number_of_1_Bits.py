#!/usr/bin/env python3


# 方法一：逐位检查
class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        while n > 0:
            if n & 1 == 1:
                w += 1
            n >>= 1
        return w


# 方法二：Brian Kernighan 算法（更快）
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
