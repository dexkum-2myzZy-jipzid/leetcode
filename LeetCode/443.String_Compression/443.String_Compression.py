#!/usr/bin/env python3


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, j = 0, 0

        while i < n:
            cur = chars[i]
            cnt = 1
            # read consecutive repeating characters
            while i + 1 < n and chars[i + 1] == cur:
                i += 1
                cnt += 1
            i += 1
            # write it into chars
            chars[j] = cur
            j += 1
            if cnt == 1:
                continue
            for d in str(cnt):
                chars[j] = d
                j += 1

        return j
