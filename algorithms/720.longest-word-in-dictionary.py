class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        m = dict({w: 1 for w in words})

        words.sort(key=lambda x: (-len(x), x))

        for word in words:
        
            def check(word):
                for i in range(1, len(word)):
                    if word[:i] not in m:
                        return False
                return True

            if check(word):
                return word
        return ''

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print Solution().longestWord(words)
