class Solution:
    # @return an integer
    def trailingZeroes(self, n):
##        m = 0
##        while n != 0:
##            n = n // 5
##            m = m + n
##        return m
        return 0 if n < 5 else n//5 + self.trailingZeroes(n//5)

print(Solution().trailingZeroes(5))
