class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==0:
            return None
        # [-2]
        maxNow=minHere0=maxHere0=A[0]
        # minHere is meant for negative number
        for i in range(1,len(A),1):
            # [-2,3,-4]
            maxHere=max(minHere0*A[i],maxHere0*A[i],A[i])
            minHere=min(minHere0*A[i],maxHere0*A[i],A[i])
            maxNow=max(maxHere, maxNow)
            maxHere0=maxHere
            minHere0=minHere
        return maxNow
    
##        # TLE
##        if len(A)==0:
##            return None
##        maxNow=A[0]
##        for i in range(len(A)):
##            curMax=1
##            for j in range(i,len(A)):
##                curMax*=A[j]
##                if curMax>maxNow:
##                    maxNow=curMax
##        return maxNow
            

for A in [-2,3,-4],[-2]:
    print(Solution().maxProduct(A))
