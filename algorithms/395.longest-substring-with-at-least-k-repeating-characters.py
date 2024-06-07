# Find the length of the longest substring T of a given string
# (consists of lowercase letters only)
# such that every character in T appears no less than k times.

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


# first thought: use a moving window
# no need to use a moving window
# use the first too rare character to split the list
