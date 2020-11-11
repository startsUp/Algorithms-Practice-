class Trie(object):
    def __init__(self):
        self.end = False
        self.c = {}

    def insert(self, word):
        node = self
        for w in word:
            if w not in node.c:
                anode.c[w] = Trie()
            node = node.c[w]
        node.end = True
            
    def prefixnode(self,word):
        node = self
        for w in word:
            if w not in node.c:
                return None
            node = node.c[w]
        return node
    
    def search(self, word):
        node = self.prefixnode(word)
        if not node:
            return False
        else:
            return True if node.end else False
            
    def startsWith(self, prefix):
        node = self.prefixnode(prefix)       
        return bool(node)        
class Solution:
    def getWords(self, board: List[List[str]], trie: Trie) -> bool:
        indx = 0
        visited = [[False for i in board[0]] for i in range(len(board))]
        def dfs(i, j, wordPrefix):
            wordPrefix += board[i][j]
            
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or visited[i][j] or (not trie.startsWith(wordPrefix)):
                return
            
            if trie.search(wordPrefix):
                words.append(wordPrefix)

            visited[i][j] = True
            dfs(i-1, j, wordPrefix)
            dfs(i+1, j, wordPrefix)
            dfs(i, j-1, wordPrefix)
            dfs(i, j+1, wordPrefix)
            visited[i][j] = False # backtrack
            
        words = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if trie.startsWith(board[i][j]):
                    dfs(i, j, '')
                        
        return words
		
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words: 
            trie.insert(w)
        return self.getWords(board, trie)
        
        
        