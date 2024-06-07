class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # >= citations[m], >= n-m
        l, r = 0, len(citations)
        while l != r:
            h = l + (r-l)//2 + 1 # whether h can be l or r.
            if citations[len(citations)-h] >= h:
                l = h
            else:
                r = h - 1
        return l
        
##        TLE
##        for r in range(n, 0, -1):
##            if citations[n-r] >= r:
##                return r
##        return 0

citations = [1,1,2,2,3,3]
print sorted(citations)
print Solution().hIndex(sorted(citations))
