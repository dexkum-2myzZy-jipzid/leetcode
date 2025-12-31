#!/usr/bin/env python3

from collections import Counter
from math import inf


class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:

        balance = Counter()
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a

        debts = [v for v in balance.values() if v != 0]
        n = len(debts)

        def dfs(i: int) -> int:
            # exit
            if i == n:
                return 0

            # do nothing
            if debts[i] == 0:
                return dfs(i + 1)

            res = inf
            for j in range(i + 1, n):
                if debts[i] * debts[j] < 0:

                    debts[j] += debts[i]
                    res = min(res, dfs(i + 1) + 1)
                    debts[j] -= debts[i]

                    if debts[j] + debts[i] == 0:
                        break

            return res

        return dfs(0)
