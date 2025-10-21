#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        # every time numBottles exchange empty water bottles
        # may has some empty water bottles

        # emptyBottle, waterbottle = func(numBottles, numExchange)

        # when to stop, it depend if we has enough emptyBottle to exchange

        res = numBottles
        # numBottles // numExchange, numBottles % numExchange
        waterBottles, empty_bottles = divmod(numBottles, numExchange)
        res += waterBottles

        while empty_bottles + waterBottles >= numExchange:
            waterBottles, empty_bottles = divmod(
                empty_bottles + waterBottles, numExchange
            )
            res += waterBottles

        return res
