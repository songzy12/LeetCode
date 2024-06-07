class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)<2:
            return len(A)
        # sorted !!!
        cur=1
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                A[cur]=A[i]
                cur+=1
        return cur
        
        

##        if len(A)==0:
##            return 0
##        d={}
##        for i in range(len(A)):
##            if A[i] not in d:
##                d[A[i]]=1
##                continue
##            A[i]=None
##        while None in A:
##            A.remove(None)
##        return len(A)

A=[1,2]
print(Solution().removeDuplicates(A))
            
            
            
