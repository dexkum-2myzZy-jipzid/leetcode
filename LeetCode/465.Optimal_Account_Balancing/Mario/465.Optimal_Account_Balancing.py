#!/usr/bin/env python3


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # backtrack
        balance = defaultdict(int)
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a

        debts = [x for x in balance.values() if x != 0]
        n = len(debts)
        # print(debts)
        res = inf

        def dfs(i):
            if i == len(debts):
                return 0

            if debts[i] == 0:
                return dfs(i + 1)

            cnt = inf
            for j in range(i + 1, n):
                if debts[i] * debts[j] < 0:
                    debts[j] += debts[i]
                    cnt = min(cnt, dfs(i + 1) + 1)
                    debts[j] -= debts[i]

                    if debts[j] + debts[i] == 0:
                        break

            return cnt if cnt != inf else 0

        return dfs(0)
