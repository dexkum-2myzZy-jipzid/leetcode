#!/usr/bin/env python3


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        n = len(req_skills)
        skill_index = {skill: i for i, skill in enumerate(req_skills)}

        # 将每个人的技能集合转为bitmask
        people_mask = []
        for skills in people:
            mask = 0
            for s in skills:
                if s in skill_index:
                    mask |= 1 << skill_index[s]
            people_mask.append(mask)

        # DP: dp[mask] = list of people
        dp = {0: []}

        for i, pmask in enumerate(people_mask):
            if pmask == 0:
                continue  # 这个人没有贡献，跳过
            # 注意：这里要用list(dp.items())避免迭代过程中修改
            for mask, team in list(dp.items()):
                new_mask = mask | pmask
                if new_mask == mask:
                    continue  # 没有增加新技能
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

        return dp[(1 << n) - 1]
