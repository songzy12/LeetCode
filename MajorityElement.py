class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):

##        # this may work for C, but not for python
##        c=0
##        for i in range(31,-1,-1):
##            n_1=[(n>>i)&1 for n in num].count(1)
##            c=c*2+(1 if n_1>len(num)//2 else 0)
##        return c

        n=0
        c=0
        for i in num:
            if n==0:
                c=i
                n=n+1
            else:
                if c==i:
                    n=n+1
                else:
                    n=n-1
        return c
        
##        i=0
##        j=1
##        while i<len(num) and j<len(num):
##            if num[i]!=num[j]:
##                num[i]=' '
##                num[j]=' '
##                while num[i]==' ':
##                    i=i+1
##                while num[j]==' ' or j<i:
##                    j=j+1
##                    if j==len(num):
##                        return num[i]
##            else:
##                j=j+1
##        return num[i]
            
            
print(Solution().majorityElement([-2147483648]))
