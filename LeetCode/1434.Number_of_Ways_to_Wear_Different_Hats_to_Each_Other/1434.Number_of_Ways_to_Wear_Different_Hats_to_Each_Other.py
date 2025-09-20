#!/usr/bin/env python3


# dfs
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # n people, 40 types of hats
        # return n ways wear diff hats

        MOD = 10**9 + 7
        n = len(hats)

        # 40 hats, n people
        hats_dic = defaultdict(list)
        for i, arr in enumerate(hats):
            for h in arr:
                hats_dic[h].append(i)

        # people[i] is a list of people who perfer this hat
        people = list(hats_dic.values())
        m = len(people)

        # dfs ith hat, mask
        @cache
        def dfs(i, mask):
            # all people has diff hats
            if mask == (1 << n) - 1:
                return 1

            # no hat
            if i >= m:
                return 0

            # no people wear ith hats
            res = dfs(i + 1, mask)

            # one person wear ith hats
            for j in people[i]:
                # j people not wear this hat
                if not mask & (1 << j):
                    new_mask = mask | (1 << j)
                    res = (res + dfs(i + 1, new_mask)) % MOD

            return res

        return dfs(0, 0)


# dp
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # n people
        n = len(hats)
        hats_to_people = defaultdict(list)
        for i, hs in enumerate(hats):
            for h in hs:
                hats_to_people[h].append(i)

        # convert this dic to arr
        hats_arr = list(hats_to_people.values())
        m = len(hats_arr)

        dp = [[0] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            people = hats_arr[i - 1]
            for mask in range(1 << n):
                # not take ith hats
                dp[i][mask] = (dp[i][mask] + dp[i - 1][mask]) % MOD
                # take ith hats
                for person in people:
                    # check person wear hat or not
                    if not mask & (1 << person):
                        new_mask = mask | (1 << person)
                        dp[i][new_mask] = (dp[i][new_mask] + dp[i - 1][mask]) % MOD

        return dp[m][(1 << n) - 1]
