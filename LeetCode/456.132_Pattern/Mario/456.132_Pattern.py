#!/usr/bin/env python3


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # monotonic stack - decreasing num

        n = len(nums)
        # handle edge case
        if n < 3:
            return False

        min_arr = [nums[0]] * n
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], nums[i])

        # monotonic stack, store k elment
        stack = []
        for j in range(n - 1, -1, -1):
            # exclude nums[j] <= nums[i] case
            if nums[j] <= min_arr[j]:
                continue
            # find i < k && nums[i] < nums[k]
            while stack and stack[-1] <= min_arr[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True

            stack.append(nums[j])

        return False


# store the second largest num using k_val
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # monotonic stack - decreasing num

        n = len(nums)
        # handle edge case
        if n < 3:
            return False

        # monotonic stack, decreasing, store j
        stack = []
        k_val = -inf

        for i in range(n - 1, -1, -1):
            current = nums[i]

            if current < k_val:
                return True

            while stack and stack[-1] < current:
                k_val = max(k_val, stack.pop())

            stack.append(current)
            # print(k_val, stack)

        return False
