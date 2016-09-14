# Given a string s and a string t, check if s is subsequence of t.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)
        return all(c in t for c in s)
        
# first thought: dp, something like edit distance?
# just check the character in s one by one
# iter(t) make it in order
