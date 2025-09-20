#!/usr/bin/env python3


class Node:

    def __init__(self):
        self.children = {}  # key: name -> Node e.g.
        self.isFile = False  # type, file or directory
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        node, last = self._search(path)

        if node.isFile:
            return [last]

        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._search(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, _ = self._search(filePath, True)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self._search(filePath)
        return node.content

    def _search(self, path, create=False):
        node = self.root
        segments = path.split("/")[1:]  # remove 0th empty space
        for p in segments:
            if p not in node.children and create:
                node.children[p] = Node()
            if p in node.children:
                node = node.children[p]

        return node, segments[-1]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
