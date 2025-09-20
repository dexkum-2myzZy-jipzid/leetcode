#!/usr/bin/env python3


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # abbr -> word
        m, n = len(word), len(abbr)
        i = 0
        j = 0  # word pointer
        num = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == "0" and num == 0:  # encouter leading zero
                    return False
                else:
                    num = num * 10 + int(abbr[i])
                    i += 1
            else:
                j += num
                if j < len(word) and abbr[i] == word[j]:
                    i += 1
                    j += 1
                    num = 0
                else:
                    return False

        if (j + num) != len(word):
            return False

        return True


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # i, word, j abbr
        m, n = len(word), len(abbr)
        i, j = 0, 0
        while i < m and j < n:

            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if abbr[j].isdigit() and abbr[j] != "0":
                    num = 0
                    while j < n and abbr[j].isdigit():
                        num = num * 10 + int(abbr[j])
                        j += 1
                    i += num
                else:
                    return False

        return i == m and j == n
