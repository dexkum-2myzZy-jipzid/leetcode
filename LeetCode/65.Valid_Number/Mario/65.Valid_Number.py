#!/usr/bin/env python3


class Solution:
    def isNumber(self, s: str) -> bool:
        # "-123.456e-789"
        # a.b[e/E]c

        # remove first sign
        def remove_sign(x):
            i = 0
            if len(x) > 0 and x[i] in "-+":
                i += 1
            return x[i:]

        # get exponent first
        s = s.replace("E", "e")
        parts = s.split("e")

        if len(parts) > 2:
            return False

        c = True
        if len(parts) == 2:
            c = remove_sign(parts[1]).isdigit()

        if not c:
            return False

        # split by "."
        base = parts[0]
        arr = base.split(".")
        if len(arr) > 2:
            return False

        a_s = remove_sign(arr[0])
        a = a_s.isdigit()
        b = True
        if len(arr) == 2:
            b = arr[1].isdigit()

            # '2.' or '.2'
            if (len(a_s) == 0 and b) or (a and len(arr[1]) == 0):
                return True

        return a and b


# deterministic finite automaton
class Solution:
    def isNumber(self, s: str) -> bool:
        # -123.456e-789
        # DFA
        # state: 0, 1(sign), 2(digits), 3(dot which has no pre digits), 4(dot which has pre digit), 5(digits)
        # 6(e/E), 7(sign), 8(digits)

        transitions = {
            0: {"sign": 1, "digit": 2, "dot": 3},
            1: {"digit": 2, "dot": 3},
            2: {"digit": 2, "dot": 4, "e": 6},
            3: {"digit": 5},
            4: {"digit": 5, "e": 6},
            5: {"digit": 5, "e": 6},
            6: {"sign": 7, "digit": 8},
            7: {"digit": 8},
            8: {"digit": 8},
        }

        # 8, 5, 4, 2
        def get_state(ch):
            if ch in "0123456789":
                return "digit"
            elif ch in "-+":
                return "sign"
            elif ch in "eE":
                return "e"
            elif ch in ".":
                return "dot"
            else:
                return ""

        state = 0
        for i, ch in enumerate(s):
            dic = transitions[state]
            cur = get_state(ch)
            if cur in dic:
                state = dic[cur]
            else:
                return False

        return True if state in [2, 4, 5, 8] else False
