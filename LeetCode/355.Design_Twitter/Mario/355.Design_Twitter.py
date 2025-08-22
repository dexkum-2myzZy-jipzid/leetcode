#!/usr/bin/env python3

import heapq
from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        self.time = 0
        self.follower = defaultdict(set)
        self.tweet = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time, tweetId))
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most tweet / ordered from most recent to least recent
        heap = []
        # add userid himself tweets
        self.follower[userId].add(userId)
        # followee
        followees = self.follower[userId]
        for followeeId in followees:
            tmp = self.tweet[followeeId]
            for i in range(len(tmp) - 1, -1, -1):
                if len(heap) < 10:
                    heapq.heappush(heap, tmp[i])
                elif len(heap) == 10 and heap[0][0] < tmp[i][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, tmp[i])
                else:
                    break

        heap.sort(key=lambda x: -x[0])
        return [t for _, t in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
