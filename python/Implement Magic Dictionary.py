# dictionary tree, then modify each char

# no need to use dictionary tree, just a set will do

from collections import defaultdict
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(set)
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for i in range(len(word)):
                self.dict[word[:i] + '*' + word[i+1:]].add(word)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool        
        """
        for i in range(len(word)):
            # if explicitly replace 26 but one chars will do
            if word[:i] + '*' + word[i+1:] in self.dict:
                if self.dict[word[:i] + '*' + word[i+1:]].difference({word}):
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
dict = ['hello', 'hallo']
obj.buildDict(dict)
word = 'hello'
param_2 = obj.search(word)
print param_2
