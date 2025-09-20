#!/usr/bin/env python3


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def get_key(s):
            res = ""
            for i in range(1, len(s)):
                dis = (ord(s[i]) - ord(s[i - 1])) % 26
                res += chr(dis + ord("a"))
            return res

        dic = defaultdict(list)

        for s in strings:
            key = get_key(s)
            dic[key].append(s)

        # print(dic)

        return [dic[k] for k in dic]
