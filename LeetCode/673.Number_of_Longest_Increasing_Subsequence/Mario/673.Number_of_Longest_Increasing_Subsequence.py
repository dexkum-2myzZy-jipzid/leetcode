#!/usr/bin/env python3


# dp with 2 states
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[1, 1] for _ in range(n)]  # LIS, the num of LIS

        for i in range(n):
            lis, num = dp[i][0], dp[i][1]
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > lis:
                        lis = dp[j][0] + 1
                        num = dp[j][1]
                    elif dp[j][0] + 1 == lis:
                        num += dp[j][1]

            dp[i] = [lis, num]

        max_lis = max(lis for lis, _ in dp)

        return sum(num for lis, num in dp if lis == max_lis)


# 二分搜索 + 树状数组
class BIT:
    def __init__(self, n):
        self.n = n
        # 存储(最大长度, 对应计数)的元组
        self.tree = [(0, 0)] * (n + 1)

    def update(self, idx, length, count):
        """更新位置idx的最大长度和计数"""
        while idx <= self.n:
            if length > self.tree[idx][0]:
                # 发现更长的子序列
                self.tree[idx] = (length, count)
            elif length == self.tree[idx][0]:
                # 相同长度，累加计数
                self.tree[idx] = (length, self.tree[idx][1] + count)
            idx += idx & (-idx)  # 移动到下一个需要更新的位置

    def query(self, idx):
        """查询1到idx范围内的最大长度和对应计数"""
        max_len = 0
        total_count = 0

        while idx > 0:
            if self.tree[idx][0] > max_len:
                max_len = self.tree[idx][0]
                total_count = self.tree[idx][1]
            elif self.tree[idx][0] == max_len:
                total_count += self.tree[idx][1]
            idx -= idx & (-idx)  # 移动到下一个需要查询的位置

        return max_len, total_count


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 坐标压缩
        sorted_nums = sorted(set(nums))
        coord_map = {v: i + 1 for i, v in enumerate(sorted_nums)}

        # 初始化树状数组
        bit = BIT(len(sorted_nums))

        # 处理每个元素
        for num in nums:
            idx = coord_map[num]

            # 查询所有小于num的元素能达到的最大长度和计数
            max_len, total_count = bit.query(idx - 1)

            # 当前元素能达到的新长度和计数
            new_len = max_len + 1
            new_count = max(1, total_count)

            # 更新树状数组
            bit.update(idx, new_len, new_count)

        # 查询最终结果
        max_len, result = bit.query(len(sorted_nums))
        return result
