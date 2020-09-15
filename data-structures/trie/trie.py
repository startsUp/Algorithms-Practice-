class TrieNode:
    def __init__(self, v, isEnd):
        self.val = v
        self.next = [None for i in range(26)]
        self.isEnd = isEnd
    def getNext(self, c):
        k = ord(c) - 97 # index
        return self.next[k]
    def setNext(self, c, node):
        k = ord(c) - 97
        self.next[k] = node
    """
    Initialize your data structure here.
        """
class Trie:
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('', False)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tempRoot = self.root
        for c in word:
            node = tempRoot.getNext(c)
            if (node):
                tempRoot = node
            else:
                newNode = TrieNode(c, False)
                tempRoot.setNext(c, newNode)
                tempRoot = newNode
        tempRoot.isEnd = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tempRoot = self.root
        for c in word:
            node = tempRoot.getNext(c)
            if (node):
                tempRoot = node
            else:
                return False
        return tempRoot.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tempRoot = self.root
        for c in prefix:
            node = tempRoot.getNext(c)
            if (node):
                tempRoot = node
            else:
                return False
        return tempRoot != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
