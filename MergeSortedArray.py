class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        
##        j=m+n-1
##        m=m-1
##        n=n-1
##        while m>=0 and n>=0:
##            if A[m]<B[n]:
##                A[j]=B[n]                
##                n-=1
##            else:
##                A[j]=A[m]
##                m-=1
##            j-=1    
##        while n>=0:
##            A[j]=B[n]
##            n-=1
##            j-=1
##        return
##

        i=0
        j=0
        while True:
            # be CAREFUL about the order!!!
            while  i<m and j<n and A[i]<=B[j]:
                    i+=1
            # here A[i]>B[j] or i=len(A) or j=len(B)
            if i==m:
                for x in B[j:]:
                    A[i]=x
                    i+=1
                return
            if j==n:
                return
            A.insert(i,B[j])
            # the true length of A will be added
            m+=1
            j+=1
            i+=1

# also care for the input format of leetcode oj
# just to notice that here len(A)!=m, here len(A)=m+n
A=[1,0]
B=[2]
Solution().merge(A,1,B,1)
print (A)


