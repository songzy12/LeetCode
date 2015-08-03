class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        table = [0 for i in range(26)]
        for i in s:
            table[ord(i)-ord('a')] += 1
        for i in t:
            if not table[ord(i)-ord('a')]:
                return False
            table[ord(i)-ord('a')] -= 1
        return True
            
s, t = "rat", "cat"
s, t = "anagram", "nagaram"
print Solution().isAnagram(s, t)
