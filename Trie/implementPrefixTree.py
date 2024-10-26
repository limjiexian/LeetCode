class TrieNode:
    def __init__(self):
        self.children = {}
        self.Terminal = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.Terminal = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
        
            curr = curr.children[c]
        
        return curr.Terminal
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
    

        