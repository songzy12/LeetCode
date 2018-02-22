class Node:
    def __init__(self):
        self.words = []
        self.next = {}
        
class SuffixTree:
    def __init__(self):
        self.root = Node()

    def add(self, word, i):
        current = self.root
        current.words = [(i, word)] + current.words
        for c in word:
            if c not in current.next:
                current.next[c] = Node()
            current.next[c].words = [(i, word)] + current.next[c].words
            current = current.next[c]

    def find(self, word):
        current = self.root
        for c in word:
            if c not in current.next:
                return []
            current = current.next[c]
        return current.words
        
    
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        def build_prefix(words):
            tree = SuffixTree()
            for i, word in enumerate(words):
                tree.add(word, i)
            return tree

        self.prefix_tree = build_prefix(words)
        self.suffix_tree = build_prefix([word[::-1] for word in words])

    
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        p = self.prefix_tree.find(prefix)
        s = self.suffix_tree.find(suffix)
        print (p, s)
        i = 0
        j = 0
        while i < len(p) and j < len(s):
            if p[i][0] > s[j][0]:
                i += 1
            elif p[i][0] < s[j][0]:
                j += 1
            else:
                return p[i][0]       
        return -1

words = ["apple", "ae", "ak", "bk", "asdk"]
obj = WordFilter(words)
param_1 = obj.f("a", "e")
param_1 = obj.f("a", "k")
print(param_1)
