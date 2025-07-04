#!/usr/bin/env python3


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # i: [0, m-1] j:[]
        # i - j = fixed num [m-1, -(n-1)]

        m, n = len(matrix), len(matrix[0])

        dic = defaultdict(int)
        for i in range(m):
            for j in range(n):
                key = i - j
                if key not in dic:
                    dic[key] = matrix[i][j]
                elif dic[key] != matrix[i][j]:
                    return False

        return True
