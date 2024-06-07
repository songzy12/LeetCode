class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        head, tail = 0, len(s) - 1
        s = list(s)
        while head < tail:
            while head < len(s) and s[head] not in 'aeiouAEIOU':
                head += 1
            while tail >= 0 and s[tail] not in 'aeiouAEIOU':
                tail -= 1
            if head < tail:
                s[head],s[tail] =  s[tail],s[head]
                head += 1
                tail -= 1
        return ''.join(s)

s = ".,"
print Solution().reverseVowels(s)
            
            
