class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    class TriNode:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.TriNode()
        self.res = []
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children: # 'app', 'apple'
                cur.children[c] = self.TriNode()
            cur = cur.children[c]
        cur.end = True
    def findWords(self, board, words):
        if not board:
            return []
        for word in words:
            self.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(self.root, board, i, j, '')
                # print(self.res)
        return self.res
    def search(self, node, board, i, j, cur):
        if node.end:
            node.end = False # avoid repetition
            self.res += [cur] # self.res += cur
        if i<0 or i==len(board) or j<0 or j== len(board[0]):
            return
        c = board[i][j]
        node = node.children.get(c, None)
        if not node:
            return
        cur += c
        board[i][j] = '-' # how can you use 'x'?!
        self.search(node, board, i+1, j, cur)
        self.search(node, board, i-1, j, cur)
        self.search(node, board, i, j+1, cur)
        self.search(node, board, i, j-1, cur)
        board[i][j] = c

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print(Solution().findWords(board, words))
