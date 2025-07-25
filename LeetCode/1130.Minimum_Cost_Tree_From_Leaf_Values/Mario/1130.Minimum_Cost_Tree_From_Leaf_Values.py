#!/usr/bin/env python3


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_leaf = [[0] * n for _ in range(n)]
        for i in range(n):
            cur = arr[i]
            for j in range(i, n):
                cur = max(cur, arr[j])
                max_leaf[i][j] = cur

        # print(max_leaf)
        # dp[i][j] means the smallest sum of arr[i:j]
        # dp[i][j] = dp[i][k] + dp[k+1][j] + max_leaf[i][k] * max_leaf[k+1][j]

        dp = [[inf] * n for _ in range(n)]

        # init
        for i in range(n):
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                for k in range(i, j):
                    print(i, k, j)
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k + 1][j] + max_leaf[i][k] * max_leaf[k + 1][j],
                    )
        # print(dp)
        return dp[0][n - 1]


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [inf]  # add sentinel to avoid out-of-bounds checks

        for num in arr:
            while stack and num >= stack[-1]:
                last = stack.pop()
                res += last * min(stack[-1], num)
            stack.append(num)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
