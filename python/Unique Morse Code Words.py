class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def encode(word):
            return ''.join(map(lambda x: code[ord(x)-ord('a')], word))
        return len(set(map(encode, words)))

words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))
