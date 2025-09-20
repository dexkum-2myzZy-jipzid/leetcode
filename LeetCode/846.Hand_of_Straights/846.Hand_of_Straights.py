#!/usr/bin/env python3

from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # edge case: hand % groupsize  != 0, return False
        # [1,2,2,3,3,4,6,7,8]

        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            while count[card] > 0:
                for i in range(groupSize):
                    num = card + i
                    if num in count and count[num] > 0:
                        count[num] -= 1
                    else:
                        return False

        return True
