"""
# 리트코드
# No. 208 / implement-trie-prefix-tree
# Python 3.x.y
# by "nno0obb"
"""


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        word = "." + word.lower() + "."
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

    def search(self, word: str) -> bool:
        word = "." + word.lower() + "."
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True

    def startsWith(self, prefix: str) -> bool:
        prefix = "." + prefix.lower()
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return any(node.keys())


def test_solution(subtests):
    with subtests.test("Example 1"):
        trie = Trie()
        trie.insert("apple")
        assert trie.search("apple") is True
        assert trie.search("app") is False
        assert trie.startsWith("app") is True
        trie.insert("app")
        assert trie.search("app") is True
