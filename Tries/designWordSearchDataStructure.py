class TriesNode:
    def __init__(self):
        self.children = {}
        self.TerminalNode = False

class WordDictionary:

    def __init__(self):
        self.root = TriesNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TriesNode()
            curr = curr.children[c]
        
        curr.TerminalNode = True

    def search(self, word: str) -> bool:
        curr = self.root

        def backtrack(curr, i):
            # base case
            if i >= len(word):
                return curr.TerminalNode

            if word[i] == ".":
                for child in curr.children:
                    if backtrack(curr.children[child], i+1):
                        return True
                return False
            elif word[i] in curr.children:
                return backtrack(curr.children[word[i]], i+1)
            else:
                return False

        return backtrack(curr, 0)
        
