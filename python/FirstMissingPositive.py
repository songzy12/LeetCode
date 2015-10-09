class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # use O(1) space but much slower
        n=len(A)
        for i in range(n):
            digit=A[i]
            # i stays the same, until all relevent numbers normal
            # then i will move to the next
            while digit<=n and digit>0 and A[digit-1]!=digit:
                A[digit-1],A[i]=A[i], A[digit-1]
                digit=A[i]
        for i in range(n):
            if A[i]!=i+1:
                return i+1
        return n+1
                
##        d={}
##        for x in A:
##            d[x]=1
##        x=1
##        while x in d:
##            x+=1
##        return x

for A in [1,2,0],[3,4,-1,1],[1]:
    print(Solution().firstMissingPositive(A))
        
