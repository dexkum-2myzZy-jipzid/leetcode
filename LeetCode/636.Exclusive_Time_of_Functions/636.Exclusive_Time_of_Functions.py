#!/usr/bin/env python3


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []  # function_id
        prev_time = 0

        for i, log in enumerate(logs):
            fid, typ, time = log.split(":")
            fid, time = int(fid), int(time)

            if typ == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:  # "end"
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res
