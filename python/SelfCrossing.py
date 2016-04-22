class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # the orientation is not relevant
        return any(d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b)
               for a, b, c, d, e, f in ((x[i:i+6] + [0] * 6)[:6] # no end check
                                        for i in xrange(len(x))))
    

x = [1, 1, 1, 1]
print Solution().isSelfCrossing(x)
