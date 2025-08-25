#!/usr/bin/env python3


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        q = deque([0])
        keys = set()

        while q:
            key = q.popleft()

            if key not in keys:
                keys.add(key)
                room = rooms[key]
                for r in room:
                    if r not in keys:
                        q.append(r)

        return len(keys) == n
