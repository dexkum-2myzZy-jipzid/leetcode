#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 <= 100:
            return 0

        count = 0
        for num in range(max(101, num1), num2 + 1):
            s = str(num)
            arr = [int(ch) for ch in s]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    count += 1
                elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                    count += 1

        return count
