class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = [0 for i in range(26)]
        
        for i in range(26):
            count[i] = s.count(chr(ord('a')+i))
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            count[ord(s[i])-ord('a')] -= 1
            if count[ord(s[i])-ord('a')] == 0:
                break
        return '' if not s else s[pos] + \
               self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))

s = "cbacdcbc"
print Solution().removeDuplicateLetters(s)
