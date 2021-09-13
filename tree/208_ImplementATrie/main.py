class Node:
    def __init__(self, children=None, terminal=False):
        self.children = children if children else dict()
        self.terminal = terminal


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:                
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.terminal = True
                
    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.terminal
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
 