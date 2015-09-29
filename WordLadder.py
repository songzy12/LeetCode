class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.add(endWord)
        queue = [(beginWord, 1)]
        ls = 'abcdefghijklmnopqrstuvwxyz'
        visited = set()
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist+1))
                            visited.add(newWord)
                            wordList.remove(newWord)
        return 0

'''
    def diff(self, word1, word2):
        ans = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                ans += 1
        return ans
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if self.diff(beginWord, endWord) == 1:
            return 2
        q = [(beginWord,1)]
        visited = [beginWord]
        while q:
            tempWord, layer = q.pop(0)
            if self.diff(tempWord, endWord) == 1:
                return layer + 1
            for word in wordList:
                if word not in visited and self.diff(tempWord, word) == 1:
                    q += [(word, layer+1)]
                    visited += word,
                    # wordList.remove(word)
        return 0
'''

beginWord = "hit"
endWord = "cog"
wordList = set(["hot","dot","dog","lot","log"])
print Solution().ladderLength(beginWord, endWord, wordList)
