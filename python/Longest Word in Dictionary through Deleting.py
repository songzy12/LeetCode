class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        # max([] + [''], key = len)
        return max(sorted(filter(isSubsequence, d)) + [''], key=len)
        
# sort d, then enumerate one by one
# it really is
