#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import heapq


class AuctionSystem:

    # items:heap: (-bidAmount, -userId)
    # if has item: {userId:bidAmount}, has this entry, if not, no this entry

    def __init__(self):
        self.rank = defaultdict(list)
        self.items = defaultdict(dict)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.items[itemId][userId] = bidAmount
        heapq.heappush(self.rank[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.items[itemId][userId] = newAmount
        heapq.heappush(self.rank[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.items[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.rank[itemId]
        if not heap:
            return -1

        while heap:
            neg_bidAmount, neg_userId = heap[0]

            if (
                itemId in self.items
                and -neg_userId in self.items[itemId]
                and -neg_bidAmount == self.items[itemId][-neg_userId]
            ):
                return -neg_userId

            heapq.heappop(heap)

        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
