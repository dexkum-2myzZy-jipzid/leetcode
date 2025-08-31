#!/usr/bin/env python3
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        friends = set(friends)

        for i in order:
            if i in friends:
                res.append(i)
        return res
