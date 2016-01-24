class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return  n > 0 and 1162261467 % n == 0
##        if not n > 0:
##            return False
##        while not n % 3:
##            n /= 3
##        return n == 1

print Solution().isPowerOfThree(7)
