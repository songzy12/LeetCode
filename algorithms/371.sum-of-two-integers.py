class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a:
            a, b = (a & b) << 1, a ^ b
            # 32-bit int
            a, b = a & 0xffffffff, b & 0xffffffff
        return -self.getSum(~b, 1) if b & (1<<31) else b
        
a, b = -12, -8
print Solution().getSum(a, b)
            
        
