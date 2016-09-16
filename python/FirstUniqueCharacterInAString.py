# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i, c in enumerate(s):
            if m[c] == 1:
                return i
        return -1
