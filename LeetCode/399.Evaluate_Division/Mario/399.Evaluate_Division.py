#!/usr/bin/env python3

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        edges = {}
        divisions = {}

        for idx, equ in enumerate(equations):
            i, j = equ[0], equ[1]
            val = values[idx]
            if i in edges:
                edges[i].append(j)
            else:
                edges[i] = [j]

            divisions[f"{i}/{j}"] = val

            if j in edges:
                edges[j].append(i)
            else:
                edges[j] = [i]

            divisions[f"{j}/{i}"] = 1/val

        visit = set()

        def dfs(query, start):
            a, b = query[0], query[1]
            if a not in visit:
                if a in edges:
                    if b in edges[a]:
                        val = divisions[f"{a}/{b}"]
                        return start * val
                    else:
                        ans = -1.0
                        for c in edges[a]:
                            val = divisions[f"{a}/{c}"]
                            visit.add(a)
                            ans = dfs([f"{c}", b], start * val)
                            visit.remove(a)
                            if ans != -1.0:
                                break
                        return ans
                else:
                    return -1.0
            else:
                return -1.0

        res = []
        for query in queries:
            res.append(dfs(query, 1))
        return res
