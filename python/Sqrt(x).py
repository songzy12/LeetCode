class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        ans = 0
        bit = 1 << 16
        while bit:
            ans |= bit
            if ans*ans > x:
                ans ^= bit
            bit >>= 1
        return ans
    
##    def mySqrt(self, x):
##        return self.auxSqrt(0, x, x)
##    def auxSqrt(self, l, r, x):
##        if l == r-1: # 0, 1, 1
##            return r if r*r <= x else l
##        temp = (l+r)//2
##        if temp*temp>x:
##            return self.auxSqrt(l, temp, x)
##        if temp*temp<x:
##            return self.auxSqrt(temp, r, x)
##        return temp

from random import randint
from math import sqrt

for i in range(10000):
    x = randint(0, 10000)
    if Solution().mySqrt(x)!=int(sqrt(x)):
        print(x, Solution().mySqrt(x), sqrt(x))
