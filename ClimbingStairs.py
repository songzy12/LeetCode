class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n<2:
            return 1
        a0=a1=1
        for i in range(1,n):
            (a0,a1)=(a1,a0+a1)
        return a1

n=3
print(Solution().climbStairs(n))
        
