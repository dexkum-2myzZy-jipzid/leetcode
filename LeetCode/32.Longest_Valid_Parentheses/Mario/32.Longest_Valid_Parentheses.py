#!/usr/bin/env python3


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                # empty stack
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n

        # "xxx ()"  dp[i] = dp[i-2] + 2
        # "xxx())"  dp[i] = s[i - dp[i-1] - 1] == "(", dp[i-2]+2

        for i in range(1, n):
            c = s[i]
            if c == ")":
                if s[i - 1] == "(":
                    pre_valid_pra = dp[i - 2] if i - 2 >= 0 else 0
                    dp[i] = pre_valid_pra + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        # print(dp)
        return max(dp)
