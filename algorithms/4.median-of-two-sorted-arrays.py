class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # to find recursive solution, you may not recurse on yourself
        # but to convert the problem to a more recursive one
        m=len(A)
        n=len(B)
        if m==0 and n==0:
            return None
        # here l=(m+n+1)/2, r=(m+n+2)/2
        # median is the lth, which means index [l-1]
        # but this is more humanic
        # when m+n is odd, l=r
        # when m+n is even, l+1=r
        l=(m+n+1)>>1
        r=(m+n+2)>>1
        # the lth of m,n elements, harmony
        return (self.getkth(A,m,B,n,l)+self.getkth(A,m,B,n,r))/2.0

    # getkth means get the kth min element of s,t
    # then this is converted into another problem
    def getkth(self,s,m,t,n,k):
        if m>n:
            # just let m<=n
            return self.getkth(t,n,s,m,k)
        if m==0:
            # for m<=n, we save n==0 case
            return t[k-1]
        if k==1:
            return min(s[0],t[0])

        # no bother, you've seen this before
        i=min(m,k//2)
        j=min(n,k//2)
        if s[i-1]>t[j-1]:
            return self.getkth(s,m,t[j:],n-j,k-j)
        else:
            return self.getkth(s[i:],m-i,t,n,k-i)

        
##        # A:0,...,m-1
##        # B:0,...,n-1
##        # after merged into m+n length array, index of median
##        # index=(m+n-1)/2 or index=((m+n)/2-1,(m+n)/2)
##        # when m==0, index=(n-1)/2; when n==0, index=(m-1)/2
##        # can merge all the cases into index=(m+n-1)/2
##        # use m,n instead of len(A),len(B) to save time
##        m=len(A)
##        n=len(B)
##        index =(m+n-1)/2
##        # if m==0:
##        #     return (B[index]+B[index+1])/2.0 if len(B)%2==0 else B[index]
##        # if n==0:
##        #     return (A[index]+A[index+1])/2.0 if len(A)%2==0 else A[index]
##        # can merge all the cases into (m==0 and n==0)
##        # cur=i+j+1
##        # when after a[i], b[j]; all is after all[i+j+1]
##        if m==0 and n==0:
##            return None
##        i=j=0
##        
##        while i<m and j<n and i+j<index:
##            if A[i]<B[j]:
##                i+=1
##            else:
##                j+=1
##        while i<m and i+j<index:
##            i+=1
##        while j<n and i+j<index:
##            j+=1
##        # at last we need (i0+1)+(j0+1)=(index+1)
##        # pick one from i, j we hava i0=i, j0=j-1 or ...
##        # so before last step: i+j=i0+j0+1=index
##        if (m+n)%2!=0:
##            if i<m and j<n:
##                if A[i]<B[j]:
##                    return A[i]
##                else:
##                    return B[j]
##            if i<m:
##                return A[i]
##            if j<n:
##                return B[j]
##        else:
##            median=[None,None]
##            # now we need two elements
##            for k in range(2):
##                if i<m and j<n:
##                    if A[i]<B[j]:
##                        median[k]=A[i]
##                        i+=1
##                    else:
##                        median[k]=B[j]
##                        j+=1
##                    # be careful about continue, not break or nothing !!!
##                    continue
##                if i<m:
##                    median[k]=A[i]
##                    i+=1
##                    continue
##                if j<n:
##                    median[k]=B[j]
##                    j+=1
##                    continue
##            return (median[1]+median[0])/2.0
            
        
A=[1,4]
B=[2,3]
print (Solution().findMedianSortedArrays(A,B))
