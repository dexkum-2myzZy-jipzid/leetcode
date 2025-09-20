#!/usr/bin/env python3


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]

        n = len(strs)
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
