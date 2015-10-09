class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        for j in range(len(s), -1, -1):
            if s[j:] in wordDict:
                break
            else:
                if not j:
                    # no suffix in wordDict
                    return []
                
        result = []
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                pre = self.wordBreak(s[i+1:], wordDict)
                result += [s[:i+1]+" "+x for x in pre]
        if s in wordDict:
            result += [s]
        return result
        
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print Solution().wordBreak(s, wordDict)
