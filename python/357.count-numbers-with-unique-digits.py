class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return 0
    
        # 021 not valid, while 201 valid
        # 01 not valid, while 201 valid
        
        f = [1 for i in range(11)]
        for i in range(1, 11):
            f[i] = f[i-1] * i
        a = [(f[10]-f[9]) / f[10-i] for i in range(n+1)]
        return sum(a) + 1
     
for n in range(12):
    print Solution().countNumbersWithUniqueDigits(n)
