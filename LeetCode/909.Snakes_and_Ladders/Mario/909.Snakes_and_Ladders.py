#!/usr/bin/env python3

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # create map r,c -> num
        # numMap = {}
        # count = 1
        # r, c = n-1, 0
        # increment = 1
        # while count <= n**2:
        #     numMap[count] = [r, c]
        #     count += 1
        #     c += increment
        #     if c > n-1 or c < 0:
        #         r -= 1
        #         increment = -increment
        #         if c > n-1: c = n-1
        #         if c < 0: c = 0

        board.reverse()

        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]

        # print(numMap)

        que = deque()
        que.append([1, 0])
        visited = set()

        while que:
            num, moves = que.popleft()

            for i in range(1, 7):
                nextNum = num+i
                if nextNum <= n*n:
                    r, c = intToPos(nextNum)
                    if board[r][c] != -1:
                        nextNum = board[r][c]
                    if nextNum == n*n:
                        return moves+1
                    if nextNum not in visited:
                        visited.add(nextNum)
                        que.append([nextNum, moves+1])
        return -1
