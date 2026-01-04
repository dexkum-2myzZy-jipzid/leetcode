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


class Solution2:
    def addOperators(self, num: str, target: int) -> list[str]:

        # backtrack
        # index: start index
        # path: expressions
        # stack: caculate

        n = len(num)
        res = []

        def backtrack(index: int, path: str, stack: list[int]):
            if index == n:
                if sum(stack) == target:
                    res.append(path)
                return

            for i in range(index, n):
                # no leading zeros
                if num[index] == "0" and i > index:
                    break

                substr = num[index : i + 1]
                val = int(substr)

                if index == 0:
                    backtrack(i + 1, path + substr, stack + [val])
                else:
                    # "+"
                    backtrack(i + 1, path + "+" + substr, stack + [val])
                    # "-"
                    backtrack(i + 1, path + "-" + substr, stack + [-val])
                    # "*"
                    new_stack = stack[:]
                    last = new_stack.pop()
                    new_stack.append(last * val)
                    backtrack(i + 1, path + "*" + substr, new_stack)

        backtrack(0, "", [])

        return res
