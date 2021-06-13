class Solution(object):
    def helper(self, l):
        if len(l) == 1:
            return l
        l = [(l[i], l[len(l)-1-i]) for i in range(len(l)/2)]
        return self.helper(tuple(l))
        
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        return str(self.helper(tuple([i for i in range(1, n+1)]))[0]).replace(' ','')

n = 8
print Solution().findContestMatch(n)
        
