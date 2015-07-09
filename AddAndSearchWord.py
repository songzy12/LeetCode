class WordDictionary:
    class Node:
        def __init__(self):
            self.end = False
            self.m = {}
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def __init__(self):
        self.root = self.Node()
    
    def addWord(self, word):
        cur = self.root
        for i in word:
            if i not in cur.m:
                cur.m[i] = self.Node()
            cur = cur.m[i]
        cur.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.auxSearch(self.root, word)

    def auxSearch(self, node, word):
        if len(word) == 0:
            return True if node.end else False
        if word[0]!='.':
            return (word[0] in node.m and
                    self.auxSearch(node.m[word[0]], word[1:]))
        for i in node.m:
            if self.auxSearch(node.m[i], word[1:]):
                return True
        return False
        

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
