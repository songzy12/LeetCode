class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1
        while n:
            n >>= 1
            cur = n & 1
            if not last ^ cur:
                return False
            last = cur
        return True

for n in [5,7,11,10]:
    print Solution().hasAlternatingBits(n)
