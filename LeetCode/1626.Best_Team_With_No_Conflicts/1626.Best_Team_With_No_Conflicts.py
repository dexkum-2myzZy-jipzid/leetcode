#!/usr/bin/env python3


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        # print(players)
        n = len(players)

        dp = [0] * n

        for i, (age_i, score_i) in enumerate(players):
            # print(i, age_i, score_i)
            dp[i] = score_i
            for j in range(i):
                age_j, score_j = players[j]
                if score_j <= score_i:
                    dp[i] = max(dp[i], score_i + dp[j])

        return max(dp)
