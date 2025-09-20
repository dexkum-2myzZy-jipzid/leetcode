#!/usr/bin/env python3


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # bfs
        def is_valid(sub):
            count = 0
            for ch in sub:
                if ch not in "()":
                    continue
                if ch == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        q = deque([s])
        vis = set()
        res = set()

        while q:
            size = len(q)

            if res:
                return list(res)

            for _ in range(size):
                cur = q.popleft()

                if is_valid(cur):
                    res.add(cur)

                # remove one '(' or ')'
                for i, c in enumerate(cur):
                    if c in "()":
                        tmp = cur[:i] + cur[i + 1 :]
                        if tmp not in vis:
                            vis.add(tmp)
                            q.append(tmp)

        return list(res)
