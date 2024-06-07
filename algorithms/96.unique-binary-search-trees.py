class Solution:
    # @return an integer
    def numTrees(self, n):
        num = [1,1]
        for i in range(2,n+1):
            s = 0
            for j in range(i):
                s += num[j]*num[i-1-j]
            num.append(s)
        return num[n]
            

##        return 1 if (n==1 or n==0) else \
##               sum([self.numTrees(x)*self.numTrees(n-1-x) for x in range(n)])
    
##        from functools import reduce
##        return 1 if (n==1 or n==0) else \
##               reduce(lambda x,y:x+y,[self.numTrees(x)*self.numTrees(n-1-x) for x in range(n)])

for n in 0,1,2,3,4:
    print(Solution().numTrees(n))
