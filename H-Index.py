class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        l = [0 for i in range(n+1)]
        for i in citations:
            if i > n:
                l[n] += 1
            else:
                l[i] += 1
        for i in range(n-1, -1, -1):
            l[i] += l[i+1]
        for i in range(n, -1, -1):
            if l[i] >= i:
                return i
            
##        if not citations:
##            return 0
##        n = len(citations)
##        l = [0 for i in range(n+1)]
##        for i in citations:
##            for j in range(0, min(i+1, n+1)):
##                l[j] += 1
##        print l
##        for i in range(n, -1, -1):
##            if l[i] >= i:
##                return i

citations = [3, 0, 6, 1, 5]
print Solution().hIndex(citations)
