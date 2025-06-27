#!/usr/bin/env python3


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # 9: 10 9 2 1001 mirror
        # 4.      2 100 not mirror

        # k = 3
        # digit num / mirror / num
        # . 1     1 - 9.         9
        #  2     11,22, ... 99  9
        #  3.    1x1, 2x2, ... 9x9 9 * 9
        # . 4.    9*9
        #  5     xzyxz  9 * 9 *9

        def check_base_k_mirror(num):
            digs = []
            while num > 0:
                digs.append(num % k)
                num //= k
            return digs == digs[::-1]

        # digit num
        dig = 1
        count = 0
        res = 0
        while count < n:
            # get pre part digit count
            pre = (dig + 1) // 2
            # pre = 2
            # e [10, 100]
            start = 10 ** (pre - 1)
            end = 10**pre
            for e in range(start, end):
                tmp = str(e)
                if dig % 2 == 1:
                    tmp += tmp[-2::-1]
                else:
                    tmp += tmp[::-1]
                num = int(tmp)
                if check_base_k_mirror(num):
                    res += num
                    count += 1
                    if count == n:
                        return res

            dig += 1

        return res
