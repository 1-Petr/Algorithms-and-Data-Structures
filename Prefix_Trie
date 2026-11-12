class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, prefix:str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return f'{True}, целое слово?: {node.is_end}'
    def delete(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if not node.is_end:
            return False
        node.is_end = False
        return True
