#!/usr/bin/env python3


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # edge case
        if src == dst:
            return 0

        min_dis = [inf] * n
        min_dis[src] = 0

        for i in range(k + 1):
            tmp = min_dis[:]
            updated = False
            for from_city, to_city, price in flights:
                # relax
                if (
                    min_dis[from_city] != inf
                    and min_dis[from_city] + price < tmp[to_city]
                ):
                    tmp[to_city] = min_dis[from_city] + price
                    updated = True

            min_dis = tmp
            # print(min_dis)
            if not updated:
                break

        return min_dis[dst] if min_dis[dst] != inf else -1
