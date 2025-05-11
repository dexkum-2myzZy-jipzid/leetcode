#!/usr/bin/env python3


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # get index of matrix
        def get_index(i, j):
            x, y = i // 3, j // 3
            return 3 * x + y

        m, n = len(board), len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    # row
                    if val not in rows[i]:
                        rows[i].add(val)
                    else:
                        return False
                    # column
                    if val not in cols[j]:
                        cols[j].add(val)
                    else:
                        return False
                    # partition
                    index = get_index(i, j)
                    if val not in boxes[index]:
                        boxes[index].add(val)
                    else:
                        return False

        return True
