#!/usr/bin/env python3


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 1. pack as many word as i can
        # 2. distributed as evenly as possible
        # 3. assigned more spaces to left > right

        def justify_line(l, r, words_len):
            # 1 word
            if l == r:
                return words[l] + " " * (maxWidth - len(words[l]))
            # > 1 words
            slots = r - l
            total_spaces = r - l + maxWidth - words_len
            avg_space = total_spaces // slots
            extra = total_spaces % slots

            line = words[l]
            for i in range(l + 1, r + 1):
                if extra > 0:
                    line += " "
                    extra -= 1
                line += " " * avg_space + words[i]

            if len(line) < maxWidth:
                line += " " * (maxWidth - len(line))
            return line

        def left_align(l, r=len(words)):
            line = words[l]
            for i in range(l + 1, r):
                line += " " + words[i]
            if len(line) < maxWidth:
                line += " " * (maxWidth - len(line))
            return line

        n = len(words)
        l = 0  # store left bound of sliding win
        cur_words_len = len(words[0])
        res = []
        for i in range(1, n):
            w = words[i]
            if cur_words_len + 1 + len(w) <= maxWidth:
                cur_words_len += 1 + len(w)
            else:
                # function to get line
                res.append(justify_line(l, i - 1, cur_words_len))
                l = i
                cur_words_len = len(w)
        # function to get last line
        res.append(left_align(l))

        return res
