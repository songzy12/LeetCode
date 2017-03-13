class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i
        
        ans = [None for _ in dict]
        
        groups = collections.defaultdict(list)
        for index, word in enumerate(dict):
            # in python, you can just make a tuple to be the key for a dict
            groups[len(word), word[0], word[-1]].append((word, index))
        
        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2, _ = enum_words[i-1]
                    p = longest_common_prefix(word, word2)
                    lcp[i] = max(lcp[i], p)
                    lcp[i-1] = max(lcp[i-1], p)
                    
            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= max(1, len(str(delta)) - 1):
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last
        
        return ans
    
# the longest common prefix of W with any other word X in G must occur with words adjacent to W, 
# so we only need to check those.
