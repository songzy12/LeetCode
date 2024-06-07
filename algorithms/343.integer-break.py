class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3**(n/3)
        if n % 3 == 1:
            return 2*2*3**((n-4)/3)
        # 3+3=2+2+2, 3*3 > 2*2*2
        return 2*3**(n/3)

n = 3
print Solution().integerBreak(n)
