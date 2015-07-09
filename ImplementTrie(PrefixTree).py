class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.m = {}
        self.end = False # insert 'ab', search 'a'
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur.m: # insert 'app', insert 'apple'
                cur.m[i] = TrieNode()
            cur = cur.m[i]
        cur.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for i in word:
            if i not in cur.m:
                return False
            cur = cur.m[i]
        return cur.end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for i in prefix:
            if i not in cur.m:
                return False
            cur = cur.m[i]
        return True
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert('ab')
print(trie.search('ab'))
