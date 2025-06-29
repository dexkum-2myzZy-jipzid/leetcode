#!/usr/bin/env python3


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        small, large = [], nums[:k]
        heapq.heapify(large)
        for i in range(k // 2):
            heapq.heappush(small, -heapq.heappop(large))

        # print(f"small:{small}, large:{large}")

        def get_median(s, l):
            if k % 2 == 1:
                return float(large[0])
            else:
                return (large[0] - small[0]) / 2.0

        res = []
        res.append(get_median(small, large))

        counter = Counter()

        for l in range(n - k):
            out_num, int_num = nums[l], nums[l + k]
            balance = 0

            # mark removed num
            counter[out_num] += 1
            balance -= 1 if out_num >= large[0] else -1

            # insert new num
            if int_num >= large[0]:
                heapq.heappush(large, int_num)
                balance += 1
            else:
                heapq.heappush(small, -int_num)
                balance -= 1

            # make balance
            if balance > 0:
                heapq.heappush(small, -heapq.heappop(large))
            if balance < 0:
                heapq.heappush(large, -heapq.heappop(small))

            # if top element should be remove (lazy deletion)
            while large and counter[large[0]] > 0:
                tmp = heapq.heappop(large)
                counter[tmp] -= 1

            while small and counter[-small[0]] > 0:
                tmp = -heapq.heappop(small)
                counter[tmp] -= 1

            res.append(get_median(small, large))

        return res
