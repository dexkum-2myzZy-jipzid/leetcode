#!/usr/bin/env python3


class Solution:
    def maximumRobots(
        self, chargeTimes: List[int], runningCosts: List[int], budget: int
    ) -> int:
        n = len(chargeTimes)
        res = 0

        q = deque([])  # store index, monotonic deque
        # sliding window
        running_sum = 0
        left = 0

        for right in range(n):
            running_sum += runningCosts[right]
            t = chargeTimes[right]
            # pop element which is smaller than current charge time
            while q and chargeTimes[q[-1]] <= t:
                q.pop()

            q.append(right)
            k = right - left + 1
            total = chargeTimes[q[0]] + k * running_sum

            # shrink sliding window
            while total > budget and left <= right:
                running_sum -= runningCosts[left]

                if left == q[0]:
                    q.popleft()
                left += 1

                if left <= right:
                    k = right - left + 1
                    total = chargeTimes[q[0]] + k * running_sum

            res = max(res, right - left + 1)

        return res
