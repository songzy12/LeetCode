class Solution:
    # @return a string
    def countAndSay(self, n):
        if n==1:
            return '1'
        s=''
        index=0
        count=1
        n0=str(self.countAndSay(n-1))
        while index<len(n0):
            # index+1=len(n0) can also be regarded as n0[index+1]!=n0[index]
            while index+1<len(n0) and n0[index+1]==n0[index]:
                index+=1
                count+=1
            s+=str(count)
            s+=n0[index]
            index+=1
            count=1
        return s

##        A=['1']
##        for i in range(1,n):
##            A.append('')
##            index=0
##            count=1
##            while index<len(A[i-1]):
##                while index+1<len(A[i-1]) and A[i-1][index+1]==A[i-1][index]:
##                    index+=1
##                    count+=1
##                A[i]+=str(count)
##                A[i]+=A[i-1][index]
##                index+=1
##                count=1
##        return A[n-1]

print(Solution().countAndSay(1))
