class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while(m >> i != n >> i):
            i += 1
        return (m >> i) << i
        
##        i = 1
##        result = 0
##        while (m >> (i-1)) > 0:
##            if (m >> i-1) & 1 == 1 and n >> i == m >> i:
##                bit = 1
##            else:
##                bit = 0
##            result += (1 << (i-1)) * bit
##            i += 1
##        return result

print(Solution().rangeBitwiseAnd(5, 7))
            
