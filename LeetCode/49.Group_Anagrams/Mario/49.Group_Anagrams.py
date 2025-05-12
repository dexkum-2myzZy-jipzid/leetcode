#!/usr/bin/env python3


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # arr = [], then based a ->z order to generate str which repesent the group
        dic = defaultdict(list)  # key: str, val: arr

        for s in strs:
            key = ("").join(sorted(s))
            dic[key].append(s)

        return [arr for arr in dic.values()]
