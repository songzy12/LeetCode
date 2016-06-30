class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # z must be multiple of gcd(x,y)
        # can find m, n such that m*x - n*y = gcd(x,y)
        return z == 0 or z % gcd(x,y) == 0

x, y, z = 3, 4, 2
print Solution().canMeasureWater(x, y, z)
