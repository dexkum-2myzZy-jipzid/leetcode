#!/usr/bin/env python3


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        m, n = len(nums1), len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]  # (sum, i, j)
        res = []
        visited = set()
        visited.add((0, 0))

        while len(res) < k:
            sum0, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return res
