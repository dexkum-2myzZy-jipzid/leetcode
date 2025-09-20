#!/usr/bin/env python3

class Solution1:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        queue = deque()
        queue.append([startGene, bank, 0])

        while queue:
            array = queue.popleft()
            # print(f'array:{array}')
            mutation, tmp, count = array[0], array[1], array[2]
            visited = []
            for str1 in tmp:
                diff_count = 0
                for c1, c2 in zip(str1, mutation):
                    if c1 != c2:
                        diff_count += 1
                        if diff_count > 1:
                            break

                if diff_count == 1:
                    if str1 == endGene:
                        return count + 1
                    else:
                        queue.append(
                            [str1, [s for s in tmp if s != str1], count+1])

        return -1


# Another Solution
class Solution2:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank.append(startGene)
        pMap = collections.defaultdict(list)
        for gene in bank:
            for i in range(len(gene)):
                pattern = gene[:i] + "*" + gene[i+1:]
                pMap[pattern].append(gene)

        q = deque([startGene])
        visited = set([startGene])
        res = 0

        while q:
            for i in range(len(q)):
                gene = q.popleft()
                if gene == endGene:
                    return res

                for j in range(len(gene)):
                    pattern = gene[:j] + "*" + gene[j+1:]
                    for nei in pMap[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1

        return -1
