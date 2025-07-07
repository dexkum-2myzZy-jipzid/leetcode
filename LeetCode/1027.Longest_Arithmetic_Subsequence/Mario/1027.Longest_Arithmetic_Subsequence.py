#!/usr/bin/env python3


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # nested loop
        # dic = {} key: seq val: indices pairs [i, j] [j, k]

        n = len(nums)
        dic = defaultdict(list)
        for i in range(n):
            for j in range(i):
                dic[nums[i] - nums[j]].append((j, i))

        res = 1
        for k in dic:
            indices = dic[k]
            indices.sort(key=lambda x: x[1])
            # print(f"k:{k}\n indices:{indices}")
            count = [0] * 1001
            for a, b in indices:
                # print(a, b)
                count[b] = count[a] + 1
                # print(count[b])
                res = max(res, count[b])

        return res + 1


# dp with defaultdict
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        res = 2
        for i in range(1, n):
            for j in range(i):
                seq = nums[i] - nums[j]
                if seq not in dp[j]:
                    dp[i][seq] = 2
                else:
                    dp[i][seq] = dp[j][seq] + 1
                res = max(res, dp[i][seq])

        return res


# dp with array
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * 1003 for _ in range(n)]
        offset = 501

        res = 2
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j] + offset
                dp[i][diff] = dp[j][diff] + 1 if dp[j][diff] > 0 else 2
                res = max(res, dp[i][diff])

        return res
