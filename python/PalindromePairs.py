class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words) < 2:
            return False
        m = {}
        for index, word in enumerate(words):
            m[word] = index

        def isPalindrome(word):
            return word == word[::-1]

        res = set()
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                if isPalindrome(word[:j]):
                    dual = word[j:][::-1]
                    if dual in m and m[dual] != i: # m[dual] differ from i
                        res.add((m[dual], i))
                if isPalindrome(word[j:]):
                    dual = word[:j][::-1]
                    if dual in m and m[dual] != i:
                        res.add((i, m[dual]))
        return [list(t) for t in res]

words = ["abcd","dcba","lls","s","sssll"]
words = ["a",""]
print Solution().palindromePairs(words)

