#!/usr/bin/env python3


# DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, path):
            # print(path)
            if l == n and r == n:
                res.append(("").join(path))
                return

            # pick (
            if l < n:
                path.append("(")
                dfs(l + 1, r, path)
                path.pop()

            # pick )
            if l > r and l <= n:
                path.append(")")
                dfs(l, r + 1, path)
                path.pop()

        dfs(0, 0, [])

        return res


# backtrack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, left, right):
            if len(path) == 2 * n:
                res.append(path)
                return
            if left < n:
                backtrack(path + "(", left + 1, right)
            if right < left:
                backtrack(path + ")", left, right + 1)

        backtrack("", 0, 0)
        return res
