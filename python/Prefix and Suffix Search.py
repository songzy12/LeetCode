# https://leetcode.com/problems/prefix-and-suffix-search/description/

class Node:
    def __init__(self):
        self.words = set()
        self.next = {}
        
class SuffixTree:
    def __init__(self):
        self.root = Node()

    def add(self, word, i):
        current = self.root
        current.words.add((i, word))
        for c in word:
            if c not in current.next:
                current.next[c] = Node()
            current.next[c].words.add((i, word))
            current = current.next[c]

    def find(self, word):
        current = self.root
        for c in word:
            if c not in current.next:
                return set()
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
        s = self.suffix_tree.find(suffix[::-1]) # NOTE: here suffix also need to be reversed
        s = set([(x[0], x[1][::-1]) for x in s]) # NOTE: remember to reverse the returned string
        # print (p, s)

        p = p.intersection(s) # NOTE: this is not union
        if not p:
            return -1
        p = sorted(list(p), key=lambda x: -x[0]) # NOTE: this should be reversed
        return p[0][0]

##        i = 0
##        j = 0
##        while i < len(p) and j < len(s):
##            if p[i][0] > s[j][0]:
##                i += 1
##            elif p[i][0] < s[j][0]:
##                j += 1
##            else:
##                return p[i][0]       
##        return -1

words = ["apple"]
obj = WordFilter(words)
param_1 = obj.f("a", "e")
print(param_1)
param_1 = obj.f("a", "k")
print(param_1)

# words = ['pop']
# obj = WordFilter(words)

# ["WordFilter","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f"]
#for prefix, suffix in [["",""],["","p"],["","op"],["","pop"],["p",""],["p","p"],["p","op"],["p","pop"],["po",""],["po","p"],["po","op"],["po","pop"],["pop",""],["pop","p"],["pop","op"],["pop","pop"],["",""],["","p"],["","gp"],["","pgp"],["p",""],["p","p"],["p","gp"],["p","pgp"],["pg",""],["pg","p"],["pg","gp"],["pg","pgp"],["pgp",""],["pgp","p"],["pgp","gp"],["pgp","pgp"]]:
#    print(prefix, suffix, obj.f(prefix, suffix))

# [null,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

words = ["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]
obj = WordFilter(words)
for prefix, suffix in [["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]:
    print(prefix, suffix, obj.f(prefix, suffix))    

