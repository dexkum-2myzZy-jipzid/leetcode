#!/usr/bin/env python3


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        matrix = ["" for _ in range(numRows)]

        j, down = 0, True
        for i, c in enumerate(s):
            matrix[j] += c
            j += 1 if down else -1
            if j == numRows - 1:
                down = False
            elif j == 0:
                down = True

        return ("").join(matrix)
