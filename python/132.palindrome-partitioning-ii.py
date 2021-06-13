class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [i-1 for i in range(n+1)]
        for i in range(0, n):
            j = 0
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
                j += 1
            j = 1
            while i-j+1>=0 and i+j<n and s[i-j+1]==s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])
                j += 1
        return cut[n]
        
##        if not s:
##            return 0
##        n = len(s)
##        pal = [[False for i in range(n)] for j in range(n)]
##        d = [0 for i in range(n)]
##        for i in range(n-1, -1, -1):
##            d[i] = n-i-1
##            for j in range(i, n):
##                if s[i] == s[j] and (j-i<2 or pal[i+1][j-1]):
##                    pal[i][j] = True
##                    if j == n-1:
##                        d[i] = 0
##                    elif d[j+1] + 1 < d[i]:
##                        d[i] = d[j+1] + 1
##        return d[0]

s = 'abcb'
print Solution().minCut(s)
                    
