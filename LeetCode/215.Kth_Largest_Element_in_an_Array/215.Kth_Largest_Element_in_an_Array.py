#!/usr/bin/env python3


# heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


# divide and conquer
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # divide and conquer
        def quick_select(l, r, i):
            if l == r:
                return nums[l]
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot = nums[r]

            # check num is smaller than pivot, then switch to left side
            j = l
            for p in range(l, r):
                if nums[p] < pivot:
                    nums[p], nums[j] = nums[j], nums[p]
                    j += 1
            # put pivot val in right place jth index
            nums[r], nums[j] = nums[j], nums[r]
            if j == i:
                return nums[j]
            elif j < i:
                return quick_select(j + 1, r, i)
            else:
                return quick_select(l, j - 1, i)

        n = len(nums)
        return quick_select(0, n - 1, n - k)
