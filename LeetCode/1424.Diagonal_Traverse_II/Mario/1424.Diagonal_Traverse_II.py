#!/usr/bin/env python3


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # (i, j)  i+j i-j
        # (0, 0)  0
        # (1, 0)  1
        # (0, 1)  1

        m = len(nums)

        dic = defaultdict(list)
        for i in range(m):
            for j in range(len(nums[i])):
                dic[i + j].append(nums[i][j])

        res = []
        for key in sorted(dic):
            res.extend(reversed(dic[key]))

        return res


# bfs
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # BFS

        n = len(nums)
        q = deque()
        q.append([0, 0])
        res = []
        while q:
            i, j = q.popleft()
            res.append(nums[i][j])
            if j == 0 and i + 1 < n:
                q.append([i + 1, j])
            if j + 1 < len(nums[i]):
                q.append([i, j + 1])

        return res
