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
                nextNum = num + i
                if nextNum <= n * n:
                    r, c = intToPos(nextNum)
                    if board[r][c] != -1:
                        nextNum = board[r][c]
                    if nextNum == n * n:
                        return moves + 1
                    if nextNum not in visited:
                        visited.add(nextNum)
                        que.append([nextNum, moves + 1])
        return -1


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # (n-1, 0) -> (0, 0)
        def num2pos(num):
            r, c = divmod(num - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        q = deque([(1, 0)])  # num, rolls
        visited = set()
        visited.add(1)

        while q:
            num, rolls = q.popleft()

            for i in range(1, 7):
                nxt = num + i
                if nxt > n * n:
                    break

                r, c = num2pos(nxt)
                val = board[r][c]

                if val != -1:
                    nxt = val

                if nxt not in visited:
                    visited.add(nxt)
                    if nxt == n * n:
                        return rolls + 1
                    q.append((nxt, rolls + 1))

        return -1
