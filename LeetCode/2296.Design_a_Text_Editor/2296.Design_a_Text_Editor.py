#!/usr/bin/env python3


class TextEditor:

    def __init__(self):
        self.str = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        i = self.cursor
        self.str = self.str[:i] + text + self.str[i:]
        self.cursor += len(text)
        # print(f"cursor:{self.cursor}\t str:{self.str}")

    def deleteText(self, k: int) -> int:
        delete_len = min(k, self.cursor)
        i, j = self.cursor - delete_len, self.cursor
        self.str = self.str[:i] + self.str[j:]
        self.cursor -= delete_len
        return j - i

    def cursorLeft(self, k: int) -> str:
        left = min(k, self.cursor)
        self.cursor -= left
        i = self.cursor
        return self.str[i - 10 : i] if i > 10 else self.str[:i]

    def cursorRight(self, k: int) -> str:
        j = self.cursor + k
        self.cursor = min(len(self.str), j)
        i = self.cursor
        return self.str[i - 10 : i] if i > 10 else self.str[:i]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)


# Stack
class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        cnt = 0
        for i in range(k):
            if self.left:
                self.left.pop()
                cnt += 1
            else:
                break
        return cnt

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if self.left:
                self.right.append(self.left.pop())
            else:
                break
        i = min(len(self.left), 10)
        return "".join(self.left[-i:])

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if self.right:
                self.left.append(self.right.pop())
            else:
                break
        i = min(len(self.left), 10)
        return "".join(self.left[-i:])
