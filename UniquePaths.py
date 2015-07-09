class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m==0 or n==0:
            return 0
        d={}
        for i in range(1,m+1):
            d[(i,1)]=1
        for j in range(1,n+1):
            d[(1,j)]=1
        for i in range(2,m+1):
            for j in range(2,n+1):
                d[(i,j)]=d[(i-1,j)]+d[(i,j-1)]
        return d[(i,j)]
        

##        if m==0 or n==0:
##            return 0
##        if m==1 and n==1:
##            return 1
##        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

for m,n in [1,1],[1,2],[2,2]:
    print(Solution().uniquePaths(m,n))
