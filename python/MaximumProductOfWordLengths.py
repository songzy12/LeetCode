class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(cmp = lambda x, y: len(y) - len(x))
        masks = [0 for i in range(len(words))]
        for i in range(len(words)):
            for c in words[i]:
                masks[i] |= 1 << ord(c)
        ans = 0
        for i in range(len(words)):
            if len(words[i]) ** 2 < ans:
                break
            for j in range(i+1, len(words)):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
        
words = ["abcdef", "abcw", "baz", "foo", "bar", "xtfn"]
print Solution().maxProduct(words)
