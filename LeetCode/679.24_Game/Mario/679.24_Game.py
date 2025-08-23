#!/usr/bin/env python3


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # 4 cards, each in [1, 9]
        n = len(cards)

        def dfs(stack):
            if len(stack) == 1:
                return abs(stack[0] - 24) < 1e-6

            m = len(stack)

            for i in range(m):
                for j in range(i + 1, m):
                    remain = [v for k, v in enumerate(stack) if k != i and k != j]

                    ops = set(
                        [
                            stack[i] + stack[j],
                            stack[i] - stack[j],
                            stack[j] - stack[i],
                            stack[i] * stack[j],
                        ]
                    )

                    if abs(stack[j]) > 1e-6:
                        ops.add(stack[i] / stack[j])
                    if abs(stack[i]) > 1e-6:
                        ops.add(stack[j] / stack[i])

                    for op in ops:
                        if dfs(remain + [op]):
                            return True

            return False

        return dfs(cards)
