#!/usr/bin/env python3

class Solution:
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
