class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        q = [0]
        v = []
        while q:
            start = q.pop(0)
            if not v.count(start):
                v += start,
                for j in range(start, len(s)):
                    if s[start:j+1] in wordDict:
                        q += j+1,
                        if j+1 == len(s):
                            return True
        return False
        
s = 'leetcode'
wordDict = set(['leet', 'code'])
print Solution().wordBreak(s, wordDict)
