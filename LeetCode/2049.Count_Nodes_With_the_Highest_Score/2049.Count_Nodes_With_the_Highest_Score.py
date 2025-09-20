#!/usr/bin/env python3


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        n = len(parents)

        # build graph { parent: children }
        graph = defaultdict(list)
        for i in range(1, n):
            p = parents[i]
            graph[p].append(i)

        count = Counter()

        # print(graph)

        @cache
        def dfs(i):
            if i not in graph:
                count[n - 1] += 1
                return 1

            arr = []
            for nei in graph[i]:
                arr.append(dfs(nei))

            val = 1
            for cnt in arr:
                val *= cnt

            cnt = sum(arr) + 1
            if n - cnt > 0:
                val *= n - cnt

            count[val] += 1

            return cnt

        dfs(0)

        # print(count)

        return count[max(count.keys())]
