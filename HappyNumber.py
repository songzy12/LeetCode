class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        cycle = set()
        while n!=1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
    
##        m = {}
##        while n!=1 and n not in m:
##            m[n] = 1
##            temp = 0
##            while n:
##                temp += (n % 10)*(n % 10)
##                n //= 10
##            n = temp
##        return True if n == 1 else False

print(Solution().isHappy(200))
