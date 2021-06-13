class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check(s[i:j]) or check(s[i+1:j+1])
        return True

# Time complexity matters
