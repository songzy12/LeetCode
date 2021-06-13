class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        m = defaultdict(dict)
        for a, b in pairs:
            m[a][b] = True
            m[b][a] = True

        def similar(word1, word2):
            if word1 == word2:
                return True
            if word1 not in m:
                return False
            if word2 not in m[word1]:
                return False
            return True
        
        if len(words1) != len(words2):
            return False
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if not similar(word1, word2):
                return False
        return True
        
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]

words1 = ["great"]
words2 = ["grat"]
# pairs = []
print(Solution().areSentencesSimilar(words1, words2, pairs))
