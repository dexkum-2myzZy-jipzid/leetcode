#!/usr/bin/env python3


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # +, -, /, *, no leading zero
        # backtrack(pre, ith num)
        # not insert: backtrack(pre, i+1) pre = pre * 10 + num
        # insert operators in i+1: pre * 10 + num backtrack(0, i+1)

        n = len(num)
        self.res = []

        # path, prev, i, last_num
        def backtrack(i, prev, path, last):
            if i == n:
                if prev == target:
                    self.res.append(path)
                return

            for j in range(i, n):
                # no leading zero

                if j != i and num[i] == "0":
                    break

                cur_str = num[i : j + 1]
                cur_val = int(cur_str)

                if i == 0:
                    # no add operator
                    backtrack(j + 1, cur_val, cur_str, cur_val)
                else:
                    # +
                    backtrack(j + 1, prev + cur_val, path + "+" + cur_str, cur_val)
                    # -
                    backtrack(j + 1, prev - cur_val, path + "-" + cur_str, -cur_val)
                    # *
                    backtrack(
                        j + 1,
                        prev - last + last * cur_val,
                        path + "*" + cur_str,
                        last * cur_val,
                    )

        backtrack(0, 0, "", 0)

        return self.res
