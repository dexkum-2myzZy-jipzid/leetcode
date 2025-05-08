#!/usr/bin/env python3


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # get diff gas[i] - cost[i]
        n = len(gas)
        diff = []
        for g, c in zip(gas, cost):
            diff.append(g - c)

        # print(diff)

        cur_tank = 0
        total_tank = 0
        start = 0

        for i, d in enumerate(diff):
            cur_tank += d
            total_tank += d

            if cur_tank < 0:
                start = i + 1
                cur_tank = 0

        return start if total_tank >= 0 else -1
