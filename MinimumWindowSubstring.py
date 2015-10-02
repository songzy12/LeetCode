class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        remaining = [0 for i in range(ord('z')+1)]
        required = len(t) # not compare one by one
        for i in t:
            remaining[ord(i)] += 1
        min_len, start, left, i = (1<<31)-1, 0, 0, 0
        while i <= len(s) and start < len(s):
            if required:
                if i == len(s):
                    break
                if remaining[ord(s[i])] > 0:
                    required -= 1
                remaining[ord(s[i])] -= 1
                i += 1
            else:
                if i - start < min_len:
                    min_len = i - start
                    left = start
                if remaining[ord(s[start])] >= 0:
                    required += 1
                remaining[ord(s[start])] += 1
                start += 1
        return s[left:left+min_len] if min_len < (1<<31)-1 else ''

s, t = 'ADOBECODEBANC', 'ABC'
print Solution().minWindow(s, t)
